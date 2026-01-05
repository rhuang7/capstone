import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        sum_digits = sum(int(d) for d in str(N))
        if N % sum_digits == 0:
            results.append("Yes")
        else:
            results.append("No")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()