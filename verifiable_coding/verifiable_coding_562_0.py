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
    
    board = []
    for _ in range(N):
        row = data[idx]
        idx += 1
        board.append(row)
    
    Q = int(data[idx])
    idx += 1
    c = list(map(int, data[idx:idx+Q]))
    idx += Q
    
    # Precompute for each possible sub-board of size k x k
    # We need to find for each possible k, the minimum number of inversions needed to make it correct
    # There are two possible correct patterns for a k x k board:
    # 1. (i + j) % 2 == 0 -> 0, else 1
    # 2. (i + j) % 2 == 0 -> 1, else 0
    
    # For each possible k, compute the minimum number of inversions needed for both patterns
    # and store it in a list min_inversions[k]
    
    # Precompute for all possible k
    min_inversions = [float('inf')] * (min(N, M) + 1)
    
    for k in range(1, min(N, M) + 1):
        # For each possible top-left corner (i, j)
        # Check if the sub-board of size k x k starting at (i, j) can be made correct
        # with at most c_i inversions
        # We need to compute for both patterns
        
        # Pattern 1: (i + j) % 2 == 0 -> 0, else 1
        # Pattern 2: (i + j) % 2 == 0 -> 1, else 0
        
        # For each possible (i, j) where i + k <= N and j + k <= M
        for i in range(N - k + 1):
            for j in range(M - k + 1):
                # Compute the number of inversions needed for both patterns
                # Pattern 1
                cnt1 = 0
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        if (x + y) % 2 == 0:
                            if board[x][y] != '0':
                                cnt1 += 1
                        else:
                            if board[x][y] != '1':
                                cnt1 += 1
                # Pattern 2
                cnt2 = 0
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        if (x + y) % 2 == 0:
                            if board[x][y] != '1':
                                cnt2 += 1
                        else:
                            if board[x][y] != '0':
                                cnt2 += 1
                # Update min_inversions[k] with the minimum of cnt1 and cnt2
                min_inversions[k] = min(min_inversions[k], cnt1, cnt2)
    
    # For each query, find the maximum k such that min_inversions[k] <= c_i
    # We can use binary search for this
    results = []
    for ci in c:
        # Binary search for the maximum k where min_inversions[k] <= ci
        low = 1
        high = min(N, M)
        best = 0
        while low <= high:
            mid = (low + high) // 2
            if min_inversions[mid] <= ci:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        results.append(best)
    
    # Output the results
    for res in results:
        print(res)

if __name__ == '__main__':
    main()