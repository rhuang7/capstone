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
        M = int(data[index + 1])
        index += 2
        
        # Check if a magical path is possible
        # A magical path is possible if the total number of cells is even and the grid is not 1x1
        # Also, for a grid with even number of cells, it's possible to have a Hamiltonian path that ends adjacent to the start
        if N * M % 2 == 0 and (N * M) != 1:
            results.append("Yes")
        else:
            results.append("No")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()