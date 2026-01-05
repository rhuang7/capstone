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
        K = int(data[idx])
        idx += 1
        uncle_johny_length = A[K-1]
        sorted_A = sorted(A)
        position = sorted_A.index(uncle_johny_length) + 1
        results.append(str(position))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()