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
        
        # Total number of ways to choose 2 distinct squares
        total_pairs = valid_squares * (valid_squares - 1) // 2
        
        # Subtract the number of pairs where the queens can see each other
        # A queen can see another if they are in the same row, column, or diagonal
        # and Chef is strictly between them
        
        same_row = 0
        same_col = 0
        same_diag = 0
        
        # Count pairs in same row (excluding Chef's position)
        for c in range(1, M+1):
            if c == Y:
                continue
            same_row += 1
        
        same_row_pairs = same_row * (same_row - 1) // 2
        
        # Count pairs in same column (excluding Chef's position)
        for r in range(1, N+1):
            if r == X:
                continue
            same_col += 1
        
        same_col_pairs = same_col * (same_col - 1) // 2
        
        # Count pairs in same diagonal (excluding Chef's position)
        # Diagonals are of two types: top-left to bottom-right and top-right to bottom-left
        
        # Top-left to bottom-right diagonal
        diag1 = []
        r, c = 1, 1
        while r <= N and c <= M:
            if r != X or c != Y:
                diag1.append((r, c))
            r += 1
            c += 1
        
        diag1_len = len(diag1)
        diag1_pairs = diag1_len * (diag1_len - 1) // 2
        
        # Top-right to bottom-left diagonal
        diag2 = []
        r, c = 1, M
        while r <= N and c >= 1:
            if r != X or c != Y:
                diag2.append((r, c))
            r += 1
            c -= 1
        
        diag2_len = len(diag2)
        diag2_pairs = diag2_len * (diag2_len - 1) // 2
        
        # Total pairs where queens can see each other
        total_seen_pairs = same_row_pairs + same_col_pairs + diag1_pairs + diag2_pairs
        
        # Valid configurations = total pairs - seen pairs
        result = total_pairs - total_seen_pairs
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()