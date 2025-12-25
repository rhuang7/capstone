from __future__ import annotations
import subprocess
import sys
from pathlib import Path

def run_many_py(
    folder: str | Path,
    pattern: str = "*.py",
    python_exe: str | None = None,
):
    folder = Path(folder)
    python_exe = python_exe or sys.executable

    files = sorted(folder.rglob(pattern))
    if not files:
        print(f"No files matched: {folder} / {pattern}")
        return 0

    ok, failed = 0, 0
    results = []

    for f in files:
        # 逐个跑：错误不会终止当前主程序
        proc = subprocess.run(
            [python_exe, str(f)],
            capture_output=True,
            text=True,
        )

        passed = (proc.returncode == 0)
        results.append((f, passed, proc.returncode, proc.stdout, proc.stderr))

        if passed:
            ok += 1
            print(f"[PASS] {f}")
        else:
            failed += 1
            print(f"[FAIL] {f} (code={proc.returncode})")
            if proc.stdout.strip():
                print("  --- stdout ---")
                print(proc.stdout.rstrip())
            if proc.stderr.strip():
                print("  --- stderr ---")
                print(proc.stderr.rstrip())
        print("-" * 60)

    print(f"Done. PASS={ok}, FAIL={failed}, TOTAL={len(files)}")

    # 你可以选择：如果有失败，最后返回非0给CI
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    # 示例：跑当前目录及子目录所有 .py
    exit_code = run_many_py("./humaneval", "*.py")
    sys.exit(exit_code)