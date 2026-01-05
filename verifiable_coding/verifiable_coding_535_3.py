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
        
        # Total possible configurations (unordered pairs)
        total_configurations = valid_squares * (valid_squares - 1) // 2
        
        # Count configurations where the two queens can see each other
        # Queens can see each other if they are on the same row, same column, or same diagonal
        # and Chef is not between them
        
        same_row = 0
        same_col = 0
        same_diag = 0
        
        # Same row
        for c in range(1, M+1):
            if c != Y:
                same_row += 1
        
        # Same column
        for r in range(1, N+1):
            if r != X:
                same_col += 1
        
        # Same diagonal (both directions)
        # Diagonal 1: r - c = X - Y
        d1 = X - Y
        count = 0
        for r in range(1, N+1):
            c = r - d1
            if 1 <= c <= M and (r != X or c != Y):
                count += 1
        same_diag += count
        
        # Diagonal 2: r + c = X + Y
        d2 = X + Y
        count = 0
        for r in range(1, N+1):
            c = d2 - r
            if 1 <= c <= M and (r != X or c != Y):
                count += 1
        same_diag += count
        
        # Total configurations where queens can see each other
        visible_configurations = same_row + same_col + same_diag
        
        # Subtract visible configurations from total
        result = total_configurations - visible_configurations
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()