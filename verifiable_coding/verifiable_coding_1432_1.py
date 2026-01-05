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
        matrix = []
        for _ in range(N):
            row = list(map(int, data[idx:idx+N]))
            idx += N
            matrix.append(row)
        
        # Count the number of 1s in the matrix
        total_ones = sum(sum(row) for row in matrix)
        
        # The minimum possible bandwidth is 0 if there are no 1s
        if total_ones == 0:
            results.append(0)
            continue
        
        # For a matrix with 1s, the minimum bandwidth is determined by the maximum number of 1s in any diagonal strip
        # We can arrange the 1s in the matrix to be as close to the diagonal as possible
        # The minimum possible bandwidth is the maximum number of 1s in any diagonal strip minus 1
        
        # Create a list to count the number of 1s in each diagonal strip
        diagonal_counts = [0] * (2 * N - 1)
        
        for i in range(N):
            for j in range(N):
                # The diagonal strip is determined by i - j
                # The value of i - j ranges from -(N-1) to N-1
                # We map this to 0 to 2N-2
                d = i - j
                if d < 0:
                    d += 2 * N - 1
                diagonal_counts[d] += matrix[i][j]
        
        # Find the maximum number of 1s in any diagonal strip
        max_ones = max(diagonal_counts)
        
        # The minimum possible bandwidth is max_ones - 1
        results.append(max_ones - 1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()