import sys
import collections

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
        
        # Count the number of square submatrices with sum X
        count = 0
        
        # For each possible square size k (from 1 to N)
        for k in range(1, N+1):
            # For each possible top-left corner (i, j)
            for i in range(N - k + 1):
                for j in range(N - k + 1):
                    # Calculate the sum of the k x k square in B
                    # B[i][j] = A[i] + A[j]
                    # Sum over all cells in the square
                    # Sum = sum_{x=i}^{i+k-1} sum_{y=j}^{j+k-1} (A[x] + A[y])
                    # = sum_{x=i}^{i+k-1} sum_{y=j}^{j+k-1} A[x] + sum_{x=i}^{i+k-1} sum_{y=j}^{j+k-1} A[y]
                    # = k * sum_{x=i}^{i+k-1} A[x] + k * sum_{y=j}^{j+k-1} A[y]
                    # = k * (sum_A[i..i+k-1] + sum_A[j..j+k-1])
                    sum_A = prefix[i+k] - prefix[i]
                    sum_B = k * (sum_A + sum_A)
                    if sum_B == X:
                        count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()