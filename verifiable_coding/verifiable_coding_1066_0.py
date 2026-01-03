import sys

def is_nice(num):
    s = str(num)
    for i in range(len(s) - 1):
        if s[i] >= s[i + 1]:
            return False
    return True

def find_largest_nice(num):
    s = list(str(num))
    length = len(s)
    for i in range(length - 1, -1, -1):
        for j in range(i + 1, length):
            if s[j] > s[i]:
                # Swap and decrease the next digit
                s[i], s[j] = s[j], s[i]
                for k in range(i + 1, length):
                    s[k] = '9'
                return int(''.join(s))
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