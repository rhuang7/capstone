import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().decode().strip()
    n = int(input)
    print(25 if n >= 2 else 25)

if __name__ == '__main__':
    solve()