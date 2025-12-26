import ast
from pathlib import Path
from typing import Optional, Tuple


def _const_int(node: ast.AST) -> Optional[int]:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value
    return None


def _range_iters(call: ast.Call) -> Optional[int]:
    if not (isinstance(call.func, ast.Name) and call.func.id == "range"):
        return None

    args = call.args
    if len(args) == 1:
        stop = _const_int(args[0])
        if stop is None:
            return None
        return max(0, stop)

    if len(args) == 2:
        start = _const_int(args[0])
        stop = _const_int(args[1])
        if start is None or stop is None:
            return None
        return max(0, stop - start)

    if len(args) == 3:
        start = _const_int(args[0])
        stop = _const_int(args[1])
        step = _const_int(args[2])
        if start is None or stop is None or step is None or step == 0:
            return None
        if step > 0:
            if start >= stop:
                return 0
            return (stop - start + step - 1) // step
        else:
            if start <= stop:
                return 0
            step = -step
            return (start - stop + step - 1) // step

    return None


def _count_asserts_in_stmts(stmts, multiplier: int) -> Tuple[int, bool]:
    total = 0
    unknown = False

    for st in stmts:
        if isinstance(st, ast.Assert):
            total += multiplier

        elif isinstance(st, ast.For):
            iters = None
            if isinstance(st.iter, ast.Call):
                iters = _range_iters(st.iter)

            if iters is None:\
                unknown = True
            else:
                sub_total, sub_unknown = _count_asserts_in_stmts(st.body, multiplier * iters)
                total += sub_total
                unknown = unknown or sub_unknown

            if st.orelse:
                sub_total, sub_unknown = _count_asserts_in_stmts(st.orelse, multiplier)
                total += sub_total
                unknown = unknown or sub_unknown

        elif isinstance(st, ast.While):
            unknown = True
            sub_total, sub_unknown = _count_asserts_in_stmts(st.body, multiplier)
            unknown = True or sub_unknown

        elif isinstance(st, (ast.If, ast.With, ast.Try, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            unknown = unknown or isinstance(st, (ast.If, ast.Try))
            for field in ("body", "orelse", "finalbody", "handlers"):
                v = getattr(st, field, None)
                if isinstance(v, list):
                    if field == "handlers":
                        for h in v:
                            sub_total, sub_unknown = _count_asserts_in_stmts(h.body, multiplier)
                            total += sub_total
                            unknown = unknown or sub_unknown
                    else:
                        sub_total, sub_unknown = _count_asserts_in_stmts(v, multiplier)
                        total += sub_total
                        unknown = unknown or sub_unknown

        else:
            pass

    return total, unknown


def estimate_assert_runs(py_path: str, func_name: str = "check") -> None:
    src = Path(py_path).read_text(encoding="utf-8")
    tree = ast.parse(src, filename=py_path)

    static_asserts = sum(isinstance(n, ast.Assert) for n in ast.walk(tree))

    target_func = None
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name == func_name:
            target_func = n
            break

    if target_func is None:
        print(f"[!] not found {func_name}()")
        print(f"static_asserts_in_file = {static_asserts}")
        return

    est, unknown = _count_asserts_in_stmts(target_func.body, multiplier=1)

    # print(f"static_asserts_in_file = {static_asserts}")
    # print(f"estimated_assert_runs_per_call_of_{func_name} = {est}")
    # print(f"has_unknown_parts = {unknown}")
    return est


# 用法示例：
# estimate_assert_runs("your_file.py", func_name="check")
