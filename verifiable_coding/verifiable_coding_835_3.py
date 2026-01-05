import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    index = 1
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        index += 2
        
        # Check if a magical path is possible
        # A magical path exists if and only if the total number of cells is even and the grid is not 1x1
        total_cells = N * M
        if total_cells % 2 == 0 and (N != 1 or M != 1):
            results.append("Yes")
        else:
            results.append("No")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()