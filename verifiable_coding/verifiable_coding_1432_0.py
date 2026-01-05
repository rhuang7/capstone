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
        N = int(data[idx])
        idx += 1
        matrix = []
        for _ in range(N):
            row = list(map(int, data[idx:idx+N]))
            idx += N
            matrix.append(row)
        
        # Count the number of 1s in the matrix
        total_ones = sum(sum(row) for row in matrix)
        
        # If there are no 1s, bandwidth is 0
        if total_ones == 0:
            results.append(0)
            continue
        
        # For a matrix with k 1s, the minimal bandwidth is the smallest k such that
        # the number of 1s can be placed in the diagonal and the first k positions around it
        # The maximum possible minimal bandwidth is N-1
        # We can use binary search to find the minimal possible bandwidth
        low = 0
        high = N - 1
        answer = N - 1
        
        while low <= high:
            mid = (low + high) // 2
            # Check if it's possible to place all 1s within a bandwidth of mid
            # We can place at most (2*mid + 1) 1s in the matrix
            # But we need to count the number of positions available in each row
            # For each row, the positions that can be filled are from i - mid to i + mid
            # But we need to ensure they are within the matrix
            # So for each row i, the positions are from max(0, i - mid) to min(N-1, i + mid)
            # The number of positions is min(N-1, i + mid) - max(0, i - mid) + 1
            # We can calculate the total number of positions available for all rows
            # If total positions >= total_ones, then it's possible
            total_positions = 0
            for i in range(N):
                start = max(0, i - mid)
                end = min(N-1, i + mid)
                total_positions += end - start + 1
            if total_positions >= total_ones:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        results.append(answer)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()