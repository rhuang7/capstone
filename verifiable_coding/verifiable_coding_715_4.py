import sys

def solve():
    import string
    s = sys.stdin.buffer.read().decode().strip()
    # Map each character to its position in the alphabet (0-based) + 28
    # A=0 -> 27, B=1 -> 28, ..., Z=25 -> 52
    # For a word, sum the values of each character
    total = 0
    for c in s:
        total += ord(c) - ord('A') + 28
    print(total)

if __name__ == '__main__':
    solve()