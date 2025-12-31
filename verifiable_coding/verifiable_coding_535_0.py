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
        # Queens can see each other if they are in the same row, column, or diagonal and Chef is not between them
        
        # Same row
        same_row = 0
        for c in range(1, M + 1):
            if c != Y:
                same_row += 1
        same_row = same_row * (same_row - 1) // 2
        
        # Same column
        same_col = 0
        for r in range(1, N + 1):
            if r != X:
                same_col += 1
        same_col = same_col * (same_col - 1) // 2
        
        # Same diagonal (both positive and negative)
        # Positive diagonal (r - c is constant)
        diag_pos = 0
        for r in range(1, N + 1):
            for c in range(1, M + 1):
                if r - c == X - Y and (r != X or c != Y):
                    diag_pos += 1
        diag_pos = diag_pos * (diag_pos - 1) // 2
        
        # Negative diagonal (r + c is constant)
        diag_neg = 0
        for r in range(1, N + 1):
            for c in range(1, M + 1):
                if r + c == X + Y and (r != X or c != Y):
                    diag_neg += 1
        diag_neg = diag_neg * (diag_neg - 1) // 2
        
        # Total configurations where queens can see each other
        total_see_each_other = same_row + same_col + diag_pos + diag_neg
        
        # Valid configurations are those where queens cannot see each other
        valid_configurations = total_configurations - total_see_each_other
        
        results.append(valid_configurations)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()