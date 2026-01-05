import sys

def min_digit(x):
    return min(int(d) for d in str(x))

def max_digit(x):
    return max(int(d) for d in str(x))

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        a1 = int(data[index])
        K = int(data[index + 1])
        index += 2
        if K == 1:
            print(a1)
            continue
        current = a1
        for _ in range(K - 1):
            m = min_digit(current)
            M = max_digit(current)
            current += m * M
        print(current)

if __name__ == '__main__':
    solve()