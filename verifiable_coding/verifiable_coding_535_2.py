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
        
        # Calculate the number of configurations where the two queens can see each other
        # Queens can see each other if they are in the same row, same column, or same diagonal
        # and Chef is strictly between them
        
        same_row = 0
        same_col = 0
        same_diag = 0
        
        # Same row
        for c in range(1, M + 1):
            if c != Y:
                same_row += 1
        
        # Same column
        for r in range(1, N + 1):
            if r != X:
                same_col += 1
        
        # Same diagonal (both positive and negative)
        # Positive diagonal (r - c is constant)
        diag1 = X - Y
        count_diag1 = 0
        for r in range(1, N + 1):
            for c in range(1, M + 1):
                if r - c == diag1 and (r != X or c != Y):
                    count_diag1 += 1
        
        # Negative diagonal (r + c is constant)
        diag2 = X + Y
        count_diag2 = 0
        for r in range(1, N + 1):
            for c in range(1, M + 1):
                if r + c == diag2 and (r != X or c != Y):
                    count_diag2 += 1
        
        same_diag = count_diag1 + count_diag2
        
        # Number of configurations where queens can see each other
        # Each line of sight has (number of squares on that line - 1) * (number of squares on that line - 2) / 2
        # But we need to count only pairs where Chef is strictly between them
        
        # Same row
        same_row_config = same_row * (same_row - 1) // 2
        
        # Same column
        same_col_config = same_col * (same_col - 1) // 2
        
        # Same diagonal
        same_diag_config = same_diag * (same_diag - 1) // 2
        
        # Total configurations where queens can see each other
        total_bad = same_row_config + same_col_config + same_diag_config
        
        # Valid configurations = total configurations - bad configurations
        valid_configurations = total_configurations - total_bad
        
        results.append(valid_configurations)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()