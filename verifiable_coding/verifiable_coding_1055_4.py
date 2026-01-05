import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    M = int(data[0])
    N = int(data[1])
    A = list(map(int, data[2:2+M]))
    
    # Initialize the maximum slices as the number of pizzas (each uncut)
    max_slices = M
    
    # We can make up to N cuts in total
    # We want to maximize the number of slices, so we should make as many cuts as possible on the pizzas with the most cuts allowed
    # Sort the array A in descending order
    A.sort(reverse=True)
    
    # We have N cuts to distribute
    # For each pizza, we can make up to A[i] cuts, and each cut increases the number of slices by 1
    # So, for each pizza, we can make min(A[i], remaining_cuts) cuts
    remaining_cuts = N
    for i in range(M):
        if remaining_cuts <= 0:
            break
        # Maximum cuts we can make on this pizza
        cuts = min(A[i], remaining_cuts)
        # Each cut increases the number of slices by 1
        max_slices += cuts
        remaining_cuts -= cuts
    
    print(max_slices)

if __name__ == '__main__':
    solve()