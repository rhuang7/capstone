import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        index += 2
        # Calculate Grundy numbers for rows and columns
        # For rows: each move reduces the row by 1, 2, or 3
        # For columns: each move reduces the column by 1 or 2
        # The game is a combination of row and column games
        # The Grundy number for a row is (N - 1) % 4
        # The Grundy number for a column is (M - 1) % 3
        # The XOR of these two gives the outcome
        row_grundy = (N - 1) % 4
        col_grundy = (M - 1) % 3
        if (row_grundy ^ col_grundy) != 0:
            print("Tuzik")
        else:
            print("Vanya")

if __name__ == '__main__':
    solve()