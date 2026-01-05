import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        total = 0
        inc = 1
        for i in range(N-1):
            if A[i] < A[i+1]:
                inc += 1
            else:
                inc = 1
            total += inc
        results.append(total)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()