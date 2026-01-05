import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        while idx < len(input) and input[idx] == b'':
            idx += 1
        if idx >= len(input):
            break
        R, C = map(int, input[idx].split())
        idx += 1
        matrix = []
        for r in range(R):
            while idx < len(input) and input[idx] == b'':
                idx += 1
            if idx >= len(input):
                break
            row = input[idx].strip()
            idx += 1
            matrix.append(row)
        found = False
        # Check rows
        for row in matrix:
            if len(row) >= 5:
                if row.lower() == 'spoon':
                    found = True
                    break
        # Check columns
        if not found:
            for c in range(C):
                col = []
                for r in range(R):
                    col.append(matrix[r][c])
                if len(col) >= 5:
                    if ''.join(col).lower() == 'spoon':
                        found = True
                        break
        print("There is a spoon!" if found else "There is indeed no spoon!")

if __name__ == '__main__':
    solve()