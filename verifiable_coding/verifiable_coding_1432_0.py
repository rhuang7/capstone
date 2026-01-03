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
        
        # For a bandwidth of k, the maximum number of 1s that can be placed is
        # sum_{i=0}^k (N - i) * 2 - 1 (for the diagonal)
        # We need to find the smallest k such that this sum >= total_ones
        
        # Try all possible k from 0 to N-1
        for k in range(N):
            max_ones = 0
            for i in range(N):
                for j in range(i - k, i + k + 1):
                    if 0 <= j < N:
                        max_ones += 1
            if max_ones >= total_ones:
                results.append(k)
                break
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()