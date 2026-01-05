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
        # Calculate the difference between each pair of consecutive plants
        # and check when their heights will be equal
        # The i-th plant grows by i per hour
        # The j-th plant grows by j per hour
        # We want A[i] + i * t = A[j] + j * t
        # => (A[i] - A[j]) = (j - i) * t
        # => t = (A[i] - A[j]) / (j - i)
        # Since A[i] > A[j], A[i] - A[j] is positive, and j - i is positive
        # So we need to find the minimum t where this equation holds for some i < j
        min_t = float('inf')
        for i in range(N-1):
            for j in range(i+1, N):
                diff = A[i] - A[j]
                growth = j - i
                if growth == 0:
                    continue
                t = diff // growth
                if diff % growth != 0:
                    continue
                if t < min_t:
                    min_t = t
        results.append(min_t)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()