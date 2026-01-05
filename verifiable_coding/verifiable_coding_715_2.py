import sys

def solve():
    import string
    s = sys.stdin.buffer.read().decode().strip()
    alphabet = string.ascii_uppercase
    values = {char: i + 28 for i, char in enumerate(alphabet)}
    total = 0
    for char in s:
        total += values[char]
    print(total)

if __name__ == '__main__':
    solve()