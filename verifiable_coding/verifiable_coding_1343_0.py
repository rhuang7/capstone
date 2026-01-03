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
    for i in range(n):
        # Remove character at position i
        new_s = s[:i] + s[i+1:]
        if len(new_s) % 2 != 0:
            continue
        half_new = len(new_s) // 2
        if new_s[:half_new] == new_s[half_new:]:
            return True
    return False

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    D = int(input[0])
    strings = input[1:D+1]
    for s in strings:
        if is_special(s):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()