import sys
import math

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        K = int(data[idx+2])
        idx += 3
        
        hearts = list(map(int, data[idx:idx+K]))
        idx += K
        
        # Convert to 0-based index
        hearts = [x-1 for x in hearts]
        
        # Convert to 2D grid coordinates
        grid = [[0]*M for _ in range(N)]
        for pos in hearts:
            row = pos // M
            col = pos % M
            grid[row][col] = 1
        
        # Precompute all possible rectangles
        # For large N and M, this is not feasible directly
        # So we use the fact that each heart contributes to some rectangles
        
        # Total number of rectangles
        total_rects = 0
        for i in range(N):
            for j in range(M):
                for k in range(i, N):
                    for l in range(j, M):
                        total_rects += 1
        
        # Count how many rectangles contain each heart
        # For each heart, count the number of rectangles that include it
        # This can be done by counting the number of rectangles that include (row, col)
        # The number of rectangles that include (row, col) is:
        # (row + 1) * (N - row) * (col + 1) * (M - col)
        # Because:
        # - The number of ways to choose the top row is (row + 1)
        # - The number of ways to choose the bottom row is (N - row)
        # - The number of ways to choose the left column is (col + 1)
        # - The number of ways to choose the right column is (M - col)
        
        # But since we have multiple hearts, we need to compute the total number of rectangles that contain at least one heart
        # However, we can't directly compute that due to overlapping
        # So we use inclusion-exclusion, but that's not feasible for K up to 1e5
        
        # So we use the linearity of expectation: the expected number of hearts is the sum over all hearts of the probability that the rectangle contains that heart
        # So for each heart, compute the number of rectangles that contain it, then divide by total_rects
        
        expected = 0.0
        for pos in hearts:
            row = pos // M
            col = pos % M
            count = (row + 1) * (N - row) * (col + 1) * (M - col)
            expected += count
        
        expected /= total_rects
        results.append(expected)
    
    for res in results:
        print(res)
        
if __name__ == '__main__':
    main()