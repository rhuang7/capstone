import sys
import bisect

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    grid = []
    for _ in range(N):
        grid.append(data[idx])
        idx += 1
    
    Q = int(data[idx])
    idx += 1
    
    c = list(map(int, data[idx:idx+Q]))
    
    # Precompute for each possible sub-board size (k x k) the minimum number of inversions needed
    # to make it a correct chessboard
    # We'll store for each possible k (from 1 to min(N, M)) the minimum number of inversions
    # required for all possible (i, j) top-left positions of a k x k sub-board
    # We'll use a 2D array for each k
    
    # Precompute for each possible k (from 1 to min(N, M)) the min inversions for all (i, j)
    max_k = min(N, M)
    min_inversions = [{} for _ in range(max_k + 1)]  # min_inversions[k] stores a 2D array for k x k sub-boards
    
    for k in range(1, max_k + 1):
        # For each possible top-left (i, j) of a k x k sub-board
        # We need to compute the number of inversions needed to make it a correct chessboard
        # There are two possible correct patterns for a k x k board:
        # 1. Starts with 0 at (i, j)
        # 2. Starts with 1 at (i, j)
        # We compute both and take the minimum
        
        # Precompute for each (i, j) the number of 0s and 1s in the k x k sub-board
        # We'll use a prefix sum approach for 0s and 1s
        # Create prefix sums for 0s and 1s
        prefix_0 = [[0]*(M+1) for _ in range(N+1)]
        prefix_1 = [[0]*(M+1) for _ in range(N+1)]
        
        for i in range(N):
            for j in range(M):
                prefix_0[i+1][j+1] = prefix_0[i][j+1] + prefix_0[i+1][j] - prefix_0[i][j] + (1 if grid[i][j] == '0' else 0)
                prefix_1[i+1][j+1] = prefix_1[i][j+1] + prefix_1[i+1][j] - prefix_1[i][j] + (1 if grid[i][j] == '1' else 0)
        
        # For each possible (i, j) top-left of a k x k sub-board
        min_inversions_k = [[float('inf')] * (M - k + 1) for _ in range(N - k + 1)]
        for i in range(N - k + 1):
            for j in range(M - k + 1):
                # Compute the number of 0s and 1s in the k x k sub-board
                # Pattern 1: starts with 0 at (i, j)
                # The number of 0s should be equal to the number of 1s, or differ by 1
                # So the number of inversions needed is the minimum between the number of 0s and 1s
                # For pattern 1, the expected number of 0s is (k*k + 1)//2 if k is odd, or k*k//2 if even
                # Similarly for pattern 2
                # But for the purpose of inversion, we can compute the number of 0s and 1s
                # and then compute the minimum number of inversions needed to make it correct
                # For a k x k board, the correct pattern has exactly (k*k + 1)//2 0s and (k*k)//2 1s
                # or vice versa
                # So the number of inversions needed is the minimum between:
                # (number of 0s - (k*k + 1)//2) if we want to make it start with 0
                # or (number of 1s - (k*k + 1)//2) if we want to make it start with 1
                # But since we can choose which pattern to use, we can take the minimum
                # So we compute the number of 0s and 1s in the sub-board
                # and then compute the minimum inversions needed for either pattern
                # Pattern 1: starts with 0
                # Pattern 2: starts with 1
                # The number of 0s in the sub-board is:
                cnt_0 = prefix_0[i+k][j+k] - prefix_0[i][j+k] - prefix_0[i+k][j] + prefix_0[i][j]
                cnt_1 = prefix_1[i+k][j+k] - prefix_1[i][j+k] - prefix_1[i+k][j] + prefix_1[i][j]
                # For pattern 1, the number of 0s should be (k*k + 1)//2
                # The number of inversions needed is abs(cnt_0 - (k*k + 1)//2)
                # For pattern 2, the number of 1s should be (k*k + 1)//2
                # The number of inversions needed is abs(cnt_1 - (k*k + 1)//2)
                # So the minimum between the two is the minimum number of inversions needed
                min_inv = min(abs(cnt_0 - (k*k + 1)//2), abs(cnt_1 - (k*k + 1)//2))
                min_inversions_k[i][j] = min_inv
        
        min_inversions[k] = min_inversions_k
    
    # Now, for each query, we need to find the maximum k such that there exists a k x k sub-board
    # that can be fixed with at most c_i inversions
    # We can precompute for each k the minimum required inversions across all possible sub-boards
    # and then for each query, perform a binary search on k
    
    # Precompute for each k the minimum required inversions across all possible sub-boards
    min_required = [float('inf')] * (max_k + 1)
    for k in range(1, max_k + 1):
        min_val = float('inf')
        for i in range(N - k + 1):
            for j in range(M - k + 1):
                if min_inversions[k][i][j] < min_val:
                    min_val = min_inversions[k][i][j]
        min_required[k] = min_val
    
    # For each query, perform binary search on k
    for ci in c:
        # Binary search for the maximum k such that min_required[k] <= ci
        low = 1
        high = max_k
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if min_required[mid] <= ci:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        print(ans)

if __name__ == '__main__':
    main()