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
    
    # We want to maximize the number of slices, so we should cut the pizzas that give the most additional slices
    # Each cut on a pizza can add at most 1 slice (if it's the first cut)
    # So we should cut the pizzas with the highest possible number of cuts first
    
    # Sort the array in descending order
    A.sort(reverse=True)
    
    # For each pizza, we can make up to A[i] cuts, but we can't exceed the remaining cuts
    for i in range(M):
        if remaining_cuts <= 0:
            break
        # The maximum number of cuts we can make on this pizza is min(A[i], remaining_cuts)
        cuts = min(A[i], remaining_cuts)
        total_slices += cuts
        remaining_cuts -= cuts
    
    print(total_slices)

if __name__ == '__main__':
    solve()