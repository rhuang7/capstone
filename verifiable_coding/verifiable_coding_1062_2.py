import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().strip()
    n = int(input)
    
    if n == 0:
        print("1")
        return
    
    for i in range(7):
        row = []
        for j in range(7):
            if i == 0 or i == 6 or j == 0 or j == 6:
                row.append(str(n))
            else:
                val = abs(i - 3) + abs(j - 3)
                row.append(str(val))
        print(' '.join(row))
    
if __name__ == '__main__':
    solve()