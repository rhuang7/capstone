import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        X = int(data[index+2])
        Y = int(data[index+3])
        index += 4
        
        total_squares = N * M
        valid_squares = total_squares - 1  # exclude Chef's position
        
        # Calculate total number of configurations
        total_configurations = valid_squares * (valid_squares - 1) // 2
        
        # Calculate number of configurations where queens can see each other
        # Queens can see each other if they are in the same row, column, or diagonal and Chef is strictly between them
        
        # Same row
        same_row = 0
        for c in range(1, M+1):
            if c != Y:
                same_row += 1
        same_row = same_row * (same_row - 1) // 2
        
        # Same column
        same_col = 0
        for r in range(1, N+1):
            if r != X:
                same_col += 1
        same_col = same_col * (same_col - 1) // 2
        
        # Same diagonal (top-left to bottom-right)
        diag1 = 0
        min_r = min(X, 1)
        max_r = max(X, N)
        min_c = min(Y, 1)
        max_c = max(Y, M)
        for r in range(min_r, max_r+1):
            c = Y + (r - X)
            if 1 <= c <= M and c != Y:
                diag1 += 1
        diag1 = diag1 * (diag1 - 1) // 2
        
        # Same diagonal (top-right to bottom-left)
        diag2 = 0
        min_r = min(X, 1)
        max_r = max(X, N)
        min_c = min(Y, M)
        max_c = max(Y, 1)
        for r in range(min_r, max_r+1):
            c = Y - (r - X)
            if 1 <= c <= M and c != Y:
                diag2 += 1
        diag2 = diag2 * (diag2 - 1) // 2
        
        # Total configurations where queens can see each other
        total_seen = same_row + same_col + diag1 + diag2
        
        # Valid configurations = total configurations - configurations where queens can see each other
        valid = total_configurations - total_seen
        
        results.append(str(valid))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()