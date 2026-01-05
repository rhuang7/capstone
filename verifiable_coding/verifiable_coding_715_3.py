import sys

def solve():
    import string
    s = sys.stdin.buffer.read().decode().strip()
    result = 0
    for char in s:
        result += ord(char) - ord('A') + 28
    print(result)

if __name__ == '__main__':
    solve()