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
        
        # Total possible configurations (unordered pairs of distinct squares)
        total_configurations = valid_squares * (valid_squares - 1) // 2
        
        # Calculate number of configurations where queens can see each other
        # Queens can see each other if they are in the same row, column, or diagonal and Chef is between them
        
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
        
        # Same diagonal (both positive and negative slope)
        # Positive slope (top-left to bottom-right)
        same_diag_pos = 0
        r, c = 1, 1
        while r <= N and c <= M:
            if r != X and c != Y:
                same_diag_pos += 1
            r += 1
            c += 1
        r, c = 1, M
        while r <= N and c >= 1:
            if r != X and c != Y:
                same_diag_pos += 1
            r += 1
            c -= 1
        
        # Negative slope (top-right to bottom-left)
        same_diag_neg = 0
        r, c = 1, M
        while r <= N and c >= 1:
            if r != X and c != Y:
                same_diag_neg += 1
            r += 1
            c -= 1
        r, c = N, 1
        while r >= 1 and c <= M:
            if r != X and c != Y:
                same_diag_neg += 1
            r -= 1
            c += 1
        
        # Total configurations where queens can see each other
        total_seen = same_row + same_col + same_diag_pos + same_diag_neg
        
        # Valid configurations are total - seen
        valid_configurations = total_configurations - total_seen
        
        results.append(valid_configurations)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()