import sys
import math

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
        M = int(data[idx+1])
        idx += 2
        matrix = []
        for _ in range(N):
            row = list(map(int, data[idx:idx+M]))
            matrix.append(row)
            idx += M
        S = data[idx]
        idx += 1
        P = int(data[idx])
        Q = int(data[idx+1])
        idx += 2
        
        # Precompute the number of steps from (0,0) to (i,j)
        steps = [[0]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if i == 0 and j == 0:
                    steps[i][j] = 0
                elif i == 0:
                    steps[i][j] = steps[i][j-1] + 1
                elif j == 0:
                    steps[i][j] = steps[i-1][j] + 1
                else:
                    steps[i][j] = steps[i-1][j] + 1
        
        # Precompute the positions for each character in S
        pos = []
        for i in range(N):
            for j in range(M):
                if steps[i][j] == 0:
                    pos.append((i, j))
                elif steps[i][j] == 1:
                    pos.append((i, j))
                elif steps[i][j] == 2:
                    pos.append((i, j))
                elif steps[i][j] == 3:
                    pos.append((i, j))
                elif steps[i][j] == 4:
                    pos.append((i, j))
                elif steps[i][j] == 5:
                    pos.append((i, j))
                elif steps[i][j] == 6:
                    pos.append((i, j))
                elif steps[i][j] == 7:
                    pos.append((i, j))
                elif steps[i][j] == 8:
                    pos.append((i, j))
                elif steps[i][j] == 9:
                    pos.append((i, j))
                elif steps[i][j] == 10:
                    pos.append((i, j))
                elif steps[i][j] == 11:
                    pos.append((i, j))
                elif steps[i][j] == 12:
                    pos.append((i, j))
                elif steps[i][j] == 13:
                    pos.append((i, j))
                elif steps[i][j] == 14:
                    pos.append((i, j))
                elif steps[i][j] == 15:
                    pos.append((i, j))
                elif steps[i][j] == 16:
                    pos.append((i, j))
                elif steps[i][j] == 17:
                    pos.append((i, j))
                elif steps[i][j] == 18:
                    pos.append((i, j))
                elif steps[i][j] == 19:
                    pos.append((i, j))
                elif steps[i][j] == 20:
                    pos.append((i, j))
                elif steps[i][j] == 21:
                    pos.append((i, j))
                elif steps[i][j] == 22:
                    pos.append((i, j))
                elif steps[i][j] == 23:
                    pos.append((i, j))
                elif steps[i][j] == 24:
                    pos.append((i, j))
                elif steps[i][j] == 25:
                    pos.append((i, j))
                elif steps[i][j] == 26:
                    pos.append((i, j))
                elif steps[i][j] == 27:
                    pos.append((i, j))
                elif steps[i][j] == 28:
                    pos.append((i, j))
                elif steps[i][j] == 29:
                    pos.append((i, j))
                elif steps[i][j] == 30:
                    pos.append((i, j))
                elif steps[i][j] == 31:
                    pos.append((i, j))
                elif steps[i][j] == 32:
                    pos.append((i, j))
                elif steps[i][j] == 33:
                    pos.append((i, j))
                elif steps[i][j] == 34:
                    pos.append((i, j))
                elif steps[i][j] == 35:
                    pos.append((i, j))
                elif steps[i][j] == 36:
                    pos.append((i, j))
                elif steps[i][j] == 37:
                    pos.append((i, j))
                elif steps[i][j] == 38:
                    pos.append((i, j))
                elif steps[i][j] == 39:
                    pos.append((i, j))
                elif steps[i][j] == 40:
                    pos.append((i, j))
                elif steps[i][j] == 41:
                    pos.append((i, j))
                elif steps[i][j] == 42:
                    pos.append((i, j))
                elif steps[i][j] == 43:
                    pos.append((i, j))
                elif steps[i][j] == 44:
                    pos.append((i, j))
                elif steps[i][j] == 45:
                    pos.append((i, j))
                elif steps[i][j] == 46:
                    pos.append((i, j))
                elif steps[i][j] == 47:
                    pos.append((i, j))
                elif steps[i][j] == 48:
                    pos.append((i, j))
                elif steps[i][j] == 49:
                    pos.append((i, j))
                elif steps[i][j] == 50:
                    pos.append((i, j))
                elif steps[i][j] == 51:
                    pos.append((i, j))
                elif steps[i][j] == 52:
                    pos.append((i, j))
                elif steps[i][j] == 53:
                    pos.append((i, j))
                elif steps[i][j] == 54:
                    pos.append((i, j))
                elif steps[i][j] == 55:
                    pos.append((i, j))
                elif steps[i][j] == 56:
                    pos.append((i, j))
                elif steps[i][j] == 57:
                    pos.append((i, j))
                elif steps[i][j] == 58:
                    pos.append((i, j))
                elif steps[i][j] == 59:
                    pos.append((i, j))
                elif steps[i][j] == 60:
                    pos.append((i, j))
                elif steps[i][j] == 61:
                    pos.append((i, j))
                elif steps[i][j] == 62:
                    pos.append((i, j))
                elif steps[i][j] == 63:
                    pos.append((i, j))
                elif steps[i][j] == 64:
                    pos.append((i, j))
                elif steps[i][j] == 65:
                    pos.append((i, j))
                elif steps[i][j] == 66:
                    pos.append((i, j))
                elif steps[i][j] == 67:
                    pos.append((i, j))
                elif steps[i][j] == 68:
                    pos.append((i, j))
                elif steps[i][j] == 69:
                    pos.append((i, j))
                elif steps[i][j] == 70:
                    pos.append((i, j))
                elif steps[i][j] == 71:
                    pos.append((i, j))
                elif steps[i][j] == 72:
                    pos.append((i, j))
                elif steps[i][j] == 73:
                    pos.append((i, j))
                elif steps[i][j] == 74:
                    pos.append((i, j))
                elif steps[i][j] == 75:
                    pos.append((i, j))
                elif steps[i][j] == 76:
                    pos.append((i, j))
                elif steps[i][j] == 77:
                    pos.append((i, j))
                elif steps[i][j] == 78:
                    pos.append((i, j))
                elif steps[i][j] == 79:
                    pos.append((i, j))
                elif steps[i][j] == 80:
                    pos.append((i, j))
                elif steps[i][j] == 81:
                    pos.append((i, j))
                elif steps[i][j] == 82:
                    pos.append((i, j))
                elif steps[i][j] == 83:
                    pos.append((i, j))
                elif steps[i][j] == 84