import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, X = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Precompute prefix sums of A
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + A[i]
        
        # For each possible square size k (from 1 to N)
        count = 0
        for k in range(1, N+1):
            # For each possible top-left corner (i, j)
            for i in range(N - k + 1):
                for j in range(N - k + 1):
                    # Compute the sum of the k x k square in B
                    # B[i][j] = A[i] + A[j]
                    # The sum of the square is sum_{x=i}^{i+k-1} sum_{y=j}^{j+k-1} (A[x] + A[y])
                    # = sum_{x=i}^{i+k-1} (k*A[x]) + sum_{y=j}^{j+k-1} (k*A[y])
                    # = k * (sum A[x] from i to i+k-1) + k * (sum A[y] from j to j+k-1)
                    # = k * (sumA[i..i+k-1] + sumA[j..j+k-1])
                    sumA1 = prefix[i+k] - prefix[i]
                    sumA2 = prefix[j+k] - prefix[j]
                    total = k * (sumA1 + sumA2)
                    if total == X:
                        count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()