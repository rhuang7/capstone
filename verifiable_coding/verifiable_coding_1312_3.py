import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        R = int(data[idx])
        C = int(data[idx+1])
        idx += 2
        
        matrix = []
        for _ in range(R):
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
                    col = []
                    for k in range(i, i + 5):
                        col.append(matrix[k][j])
                    if ''.join(col).lower() == "spoon":
                        found = True
                        break
                if found:
                    break
        
        results.append("There is a spoon!" if found else "There is indeed no spoon!")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()