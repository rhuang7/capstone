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
        
        # Check if a Hamiltonian path exists that ends at a neighboring cell
        # A Hamiltonian path exists if and only if the grid has an odd number of cells
        # and the grid is either 1x1, 1x2, 2x2, or 1x3, 3x1, 2x3, 3x2
        total = N * M
        if total % 2 == 0:
            results.append("No")
            continue
        
        # Check if the grid is 1x1
        if N == 1 and M == 1:
            results.append("Yes")
            continue
        
        # Check if the grid is 1x2, 2x1, 2x2, 1x3, 3x1, 2x3, 3x2
        if (N == 1 and M == 2) or (N == 2 and M == 1) or (N == 2 and M == 2) or (N == 1 and M == 3) or (N == 3 and M == 1) or (N == 2 and M == 3) or (N == 3 and M == 2):
            results.append("Yes")
        else:
            results.append("No")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()