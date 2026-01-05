import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    for _ in range(T):
        R = int(data[idx])
        C = int(data[idx+1])
        idx += 2
        
        matrix = []
        for i in range(R):
            row = data[idx]
            matrix.append(row)
            idx += 1
        
        found = False
        # Check rows
        for i in range(R):
            for j in range(C - 4):
                if matrix[i][j:j+5].lower() == "spoon":
                    found = True
                    break
            if found:
                break
        # Check columns
        if not found:
            for j in range(C):
                for i in range(R - 4):
                    if matrix[i][j].lower() == "s" and matrix[i+1][j].lower() == "p" and matrix[i+2][j].lower() == "o" and matrix[i+3][j].lower() == "o" and matrix[i+4][j].lower() == "n":
                        found = True
                        break
                if found:
                    break
        
        if found:
            print("There is a spoon!")
        else:
            print("There is indeed no spoon!")

if __name__ == '__main__':
    solve()