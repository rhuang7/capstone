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
        
        # For a matrix with 1s, the minimum possible bandwidth is the smallest k such that
        # there are at least (k+1)*k/2 + 1 ones in the matrix. This is because the diagonal
        # and the k bands around it contain (k+1)*k/2 + 1 elements.
        # We find the smallest k such that (k+1)*k/2 + 1 <= total_ones
        k = 0
        while (k + 1) * k // 2 + 1 <= total_ones:
            k += 1
        results.append(k - 1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()