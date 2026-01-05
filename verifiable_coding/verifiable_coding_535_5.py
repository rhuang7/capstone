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
        
        # Calculate number of configurations where queens can see each other
        # Queens can see each other if they are in the same row, column, or diagonal and Chef is between them
        
        # Count number of squares in same row (excluding Chef's position)
        same_row = (N - 1)  # exclude Chef's position
        
        # Count number of squares in same column (excluding Chef's position)
        same_col = (M - 1)  # exclude Chef's position
        
        # Count number of squares in same diagonal (excluding Chef's position)
        # Diagonals are of two types: top-left to bottom-right and top-right to bottom-left
        
        # Top-left to bottom-right diagonal
        d1 = 0
        for i in range(1, N+1):
            for j in range(1, M+1):
                if abs(i - X) == abs(j - Y):
                    d1 += 1
        d1 -= 1  # exclude Chef's position
        
        # Top-right to bottom-left diagonal
        d2 = 0
        for i in range(1, N+1):
            for j in range(1, M+1):
                if i + j == X + Y:
                    d2 += 1
        d2 -= 1  # exclude Chef's position
        
        # Total queens that can see each other
        can_see = same_row + same_col + d1 + d2
        
        # Each pair of queens that can see each other is counted twice (queen1, queen2) and (queen2, queen1)
        # So total configurations where queens can see each other is can_see * (can_see - 1) // 2
        
        configurations_where_see = can_see * (can_see - 1) // 2
        
        # Answer is total configurations minus configurations where queens can see each other
        answer = total_configurations - configurations_where_see
        
        results.append(answer)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()