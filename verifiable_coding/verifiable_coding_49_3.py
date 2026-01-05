import sys

def is_classy(x):
    s = str(x)
    return s.count('0') == len(s) - s.count('0')

def count_classy(n):
    count = 0
    for i in range(1, n + 1):
        if is_classy(i):
            count += 1
    return count

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        L = int(data[idx])
        R = int(data[idx + 1])
        idx += 2
        res = count_classy(R) - count_classy(L - 1)
        results.append(res)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()