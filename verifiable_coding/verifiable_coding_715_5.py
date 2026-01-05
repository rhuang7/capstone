import sys

def solve():
    import string
    s = sys.stdin.buffer.read().strip().decode()
    alphabet = string.ascii_uppercase
    values = {char: i + 28 for i, char in enumerate(alphabet)}
    result = sum(values[c] for c in s)
    print(result)

if __name__ == '__main__':
    solve()