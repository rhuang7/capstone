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
        grid = [[False for _ in range(M)] for _ in range(N)]
        for pos in hearts:
            row = pos // M
            col = pos % M
            grid[row][col] = True
        
        # Precompute all possible rectangles
        total_rectangles = 0
        total_hearts = 0
        
        # Iterate over all possible top-left and bottom-right corners
        for top in range(N):
            for left in range(M):
                for bottom in range(top, N):
                    for right in range(left, M):
                        # Count number of hearts in this rectangle
                        count = 0
                        for i in range(top, bottom + 1):
                            for j in range(left, right + 1):
                                if grid[i][j]:
                                    count += 1
                        # Add to total
                        total_rectangles += 1
                        total_hearts += count
        
        # Compute expected value
        expected = total_hearts / total_rectangles
        results.append(f"{expected:.15f}")
    
    print("\n".join(results))

if __name__ == '__main__':
    main()