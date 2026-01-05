import sys

def is_classy(x):
    s = str(x)
    non_zero_count = sum(1 for c in s if c != '0')
    return non_zero_count <= 3

def count_classy_up_to(n):
    count = 0
    for x in range(1, n + 1):
        if is_classy(x):
            count += 1
    return count

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        L = int(data[index])
        R = int(data[index + 1])
        index += 2
        res = count_classy_up_to(R) - count_classy_up_to(L - 1)
        results.append(res)
    for r in results:
        print(r)

if __name__ == '__main__':
    solve()