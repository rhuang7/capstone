import sys

def is_nice(num):
    s = str(num)
    for i in range(len(s) - 1):
        if s[i] >= s[i + 1]:
            return False
    return True

def find_largest_nice(n):
    s = str(n)
    length = len(s)
    for i in range(length - 1, -1, -1):
        for j in range(i, -1, -1):
            if j == i:
                current = s[:i] + s[j]
            else:
                current = s[:i] + s[j] + '9' * (length - j - 1)
            if is_nice(int(current)):
                return int(current)
    return 0

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    t = int(input[0])
    for i in range(1, t + 1):
        n = int(input[i])
        print(find_largest_nice(n))

if __name__ == '__main__':
    solve()