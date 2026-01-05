import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    M = int(data[0])
    N = int(data[1])
    A = list(map(int, data[2:2+M]))
    
    # We can make at most N cuts in total
    # For each pizza, we can make up to A[i] cuts
    # The maximum number of slices for a pizza is 1 + number of cuts (each cut increases slices by 1)
    # So we want to distribute the N cuts to maximize the sum of (1 + cuts[i])
    # Which is equivalent to maximizing the sum of cuts[i], since 1 is added for each pizza
    
    # We can use a greedy approach: assign as many cuts as possible to the pizzas with the highest A[i]
    # Sort A in descending order
    A.sort(reverse=True)
    
    # Initialize the number of cuts used
    cuts_used = 0
    # Initialize the total slices
    total_slices = M  # each pizza starts as 1 slice
    
    for i in range(M):
        # The maximum cuts we can make for this pizza is min(A[i], remaining cuts)
        max_cuts = min(A[i], N - cuts_used)
        # Add the number of cuts to the total slices
        total_slices += max_cuts
        # Update the cuts used
        cuts_used += max_cuts
        # If we have used all N cuts, break
        if cuts_used == N:
            break
    
    print(total_slices)

if __name__ == '__main__':
    solve()