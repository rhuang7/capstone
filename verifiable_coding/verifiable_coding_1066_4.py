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
    result = ''
    for i in range(length):
        if i == 0:
            result += '9'
        else:
            result += '9' * (length - i)
    return int(result)

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    t = int(input[0])
    for i in range(1, t + 1):
        n = int(input[i])
        s = str(n)
        length = len(s)
        result = ''
        for i in range(length):
            if i == 0:
                result += '9'
            else:
                result += '9' * (length - i)
        print(result)

if __name__ == '__main__':
    solve()