import sys

def solve():
    input = sys.stdin.buffer.read().decode().strip()
    n = int(input)
    
    if n == 0:
        print("1")
        return
    
    for i in range(7):
        if i == 0 or i == 6:
            print("4" * 7)
        else:
            row = []
            for j in range(7):
                if j == 0 or j == 6:
                    row.append("4")
                else:
                    row.append(str(abs(n - (i - 1) - 1)))
            print(" ".join(row))
    
if __name__ == '__main__':
    solve()