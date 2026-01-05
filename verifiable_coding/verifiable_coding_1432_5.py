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
            matrix.append(row)
            idx += N
        
        # Count the number of 1s in the matrix
        total_ones = sum(sum(row) for row in matrix)
        
        # The minimum possible bandwidth is 0 if there are no 1s
        if total_ones == 0:
            results.append(0)
            continue
        
        # For a matrix with 1s, the minimum possible bandwidth is determined by the maximum number of 1s that can be placed on a diagonal of width K
        # We try all possible K from 0 to N-1
        min_bandwidth = N - 1
        for K in range(N):
            # Count how many 1s can be placed on the main diagonal and the K bands around it
            count = 0
            for i in range(N):
                for j in range(max(0, i - K), min(N, i + K + 1)):
                    count += matrix[i][j]
            if count >= total_ones:
                min_bandwidth = K
                break
        
        results.append(min_bandwidth)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()