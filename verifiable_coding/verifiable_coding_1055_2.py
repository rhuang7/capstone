import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    M = int(data[0])
    N = int(data[1])
    A = list(map(int, data[2:2+M]))
    
    total_slices = M  # Initially, each pizza is 1 slice
    remaining_cuts = N
    
    # Sort pizzas by maximum allowed cuts in descending order
    A.sort(reverse=True)
    
    for i in range(M):
        # Use as many cuts as possible on this pizza
        cuts = min(remaining_cuts, A[i])
        total_slices += cuts
        remaining_cuts -= cuts
    
    print(total_slices)

if __name__ == '__main__':
    solve()