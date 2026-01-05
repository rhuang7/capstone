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
    result = []
    for i in range(length):
        if i == 0 and s[i] == '0':
            continue
        for j in range(i + 1, length):
            if s[j] >= s[i]:
                break
        else:
            result.append(s[i])
    if not result:
        return 0
    return int(''.join(result))

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    t = int(input[0])
    for i in range(1, t + 1):
        n = int(input[i])
        print(find_largest_nice(n))

if __name__ == '__main__':
    solve()