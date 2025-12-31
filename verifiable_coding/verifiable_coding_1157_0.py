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
        total_rectangles = 0
        total_hearts = 0
        
        # Iterate over all possible top-left and bottom-right corners
        for i in range(N):
            for j in range(M):
                for k in range(i, N):
                    for l in range(j, M):
                        # Count hearts in rectangle (i,j) to (k,l)
                        cnt = 0
                        for x in range(i, k+1):
                            for y in range(j, l+1):
                                cnt += grid[x][y]
                        total_rectangles += 1
                        total_hearts += cnt
        
        # Compute expected value
        expected = total_hearts / total_rectangles
        results.append(f"{expected:.12f}")
    
    print("\n".join(results))

if __name__ == '__main__':
    main()