import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        result = []
        for a in A:
            if a <= N:
                result.append(A[a-1])
            else:
                while a > N:
                    a //= 2
                result.append(A[N - a])
        print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()