# run_soft_asserts.py
import ast
import sys
from pathlib import Path


class SoftAssertTransformer(ast.NodeTransformer):
    def __init__(self):
        super().__init__()
        self.assert_total = 0

    def visit_FunctionDef(self, node: ast.FunctionDef):
        if node.name != "check":
            return self.generic_visit(node)

        new_body = []

        new_body.append(
            ast.Global(
                names=[
                    "__softassert_pass__",
                    "__softassert_fail__",
                    "__softassert_error__",
                    "__softassert_errors__",
                ]
            )
        )

        for stmt in node.body:
            stmt = self.visit(stmt) 
            if isinstance(stmt, list):
                new_body.extend(stmt)
            else:
                new_body.append(stmt)

        node.body = new_body
        return node

    def visit_Assert(self, node: ast.Assert):
        # Let:
        #   assert EXPR
        # Reform to:
        #   try:
        #       assert EXPR
        #       __softassert_pass__ += 1
        #   except AssertionError:
        #       __softassert_fail__ += 1
        #   except Exception as e:
        #       __softassert_error__ += 1
        #       __softassert_errors__.append(repr(e))
        self.assert_total += 1

        inc_pass = ast.AugAssign(
            target=ast.Name(id="__softassert_pass__", ctx=ast.Store()),
            op=ast.Add(),
            value=ast.Constant(1),
        )
        inc_fail = ast.AugAssign(
            target=ast.Name(id="__softassert_fail__", ctx=ast.Store()),
            op=ast.Add(),
            value=ast.Constant(1),
        )
        inc_err = ast.AugAssign(
            target=ast.Name(id="__softassert_error__", ctx=ast.Store()),
            op=ast.Add(),
            value=ast.Constant(1),
        )
        append_err = ast.Expr(
            value=ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id="__softassert_errors__", ctx=ast.Load()),
                    attr="append",
                    ctx=ast.Load(),
                ),
                args=[ast.Call(func=ast.Name(id="repr", ctx=ast.Load()), args=[ast.Name(id="e", ctx=ast.Load())], keywords=[])],
                keywords=[],
            )
        )

        try_node = ast.Try(
            body=[node, inc_pass],
            handlers=[
                ast.ExceptHandler(type=ast.Name(id="AssertionError", ctx=ast.Load()), name=None, body=[inc_fail]),
                ast.ExceptHandler(type=ast.Name(id="Exception", ctx=ast.Load()), name="e", body=[inc_err, append_err]),
            ],
            orelse=[],
            finalbody=[],
        )

        return ast.copy_location(try_node, node)


def run_file(path: str):
    code = Path(path).read_text(encoding="utf-8")
    tree = ast.parse(code, filename=path)

    transformer = SoftAssertTransformer()
    tree = transformer.visit(tree)
    ast.fix_missing_locations(tree)

    g = {
        "__name__": "__main__",
        "__softassert_pass__": 0,
        "__softassert_fail__": 0,
        "__softassert_error__": 0,
        "__softassert_errors__": [],
    }

    compiled = compile(tree, filename=path, mode="exec")
    exec(compiled, g, g)

    total = transformer.assert_total
    passed = g["__softassert_pass__"]
    failed = g["__softassert_fail__"]
    errored = g["__softassert_error__"]

    print(f"Total asserts in check(): {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Errored (non-Assertion exceptions): {errored}")

    if g["__softassert_errors__"]:
        preview = g["__softassert_errors__"][:5]
        print("Error examples (up to 5):")
        for i, e in enumerate(preview, 1):
            print(f"  {i}. {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_actual_run.py <target_file.py>")
        sys.exit(1)
    run_file(sys.argv[1])
