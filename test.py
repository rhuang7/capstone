import subprocess, sys, tempfile, textwrap

def normalize(s: str) -> str:
    # common: ignore trailing spaces and trailing newlines
    lines = s.replace("\r\n", "\n").split("\n")
    lines = [ln.rstrip() for ln in lines]
    return "\n".join(lines).rstrip() + "\n"

def run_on_input(py_file: str, inp: str, timeout_s: float = 2.0) -> tuple[int, str, str]:
    proc = subprocess.run(
        [sys.executable, py_file],
        input=inp,
        text=True,
        capture_output=True,
        timeout=timeout_s,
    )
    return proc.returncode, proc.stdout, proc.stderr

a, b, c = run_on_input('./verifiable_coding/verifiable_coding_1_0.py', "2\n4\n0\n00\n1\n11\n1\n10\n")



print(b)