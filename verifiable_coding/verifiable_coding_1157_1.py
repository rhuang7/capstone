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
        
        # Precompute all positions
        positions = [0] * (N * M)
        for pos in hearts:
            positions[pos] = 1
        
        # Count all possible rectangles
        total_rectangles = 0
        for i in range(N):
            for j in range(M):
                for k in range(i, N):
                    for l in range(j, M):
                        total_rectangles += 1
        
        # Count total hearts in all rectangles
        total_hearts = 0
        for i in range(N):
            for j in range(M):
                for k in range(i, N):
                    for l in range(j, M):
                        cnt = 0
                        for x in range(i, k):
                            for y in range(j, l):
                                cnt += positions[x * M + y]
                        total_hearts += cnt
        
        expected = total_hearts / total_rectangles
        results.append("{0:.12f}".format(expected))
    
    print("\n".join(results))

if __name__ == '__main__':
    main()