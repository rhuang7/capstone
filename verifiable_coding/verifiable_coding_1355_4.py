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
        output = []
        for a in A:
            if a <= N:
                output.append(A[a-1])
            else:
                while a > N:
                    a //= 2
                output.append(A[N - a])
        results.append(' '.join(map(str, output)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()