import sys

def is_special(s):
    n = len(s)
    if n % 2 != 0:
        return False
    half = n // 2
    # Check if the string is already a double string
    if s[:half] == s[half:]:
        return True
    # Check if removing one character can make it a double string
    for i in range(half):
        # Remove character at i from the first half
        if s[:i] + s[i+1:half] == s[half:]:
            return True
    for i in range(half, n):
        # Remove character at i from the second half
        if s[:half] == s[i+1:]:
            return True
    return False

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    D = int(data[0])
    results = []
    for i in range(1, D + 1):
        s = data[i]
        results.append("YES" if is_special(s) else "NO")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()