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
        
        # Check if a Hamiltonian path exists that ends adjacent to the start
        # A Hamiltonian path that visits all cells exactly once and ends adjacent to the start
        # is possible only if the grid has an even number of cells or if it's a 1x1 grid
        # For a grid with even number of cells, it's possible to have such a path
        # For a grid with odd number of cells, it's not possible
        # Also, for 1x1 grid, it's trivially possible
        if N * M == 1:
            results.append("Yes")
        elif (N * M) % 2 == 0:
            results.append("Yes")
        else:
            results.append("No")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()