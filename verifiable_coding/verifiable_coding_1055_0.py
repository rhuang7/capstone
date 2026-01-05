import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    M = int(data[0])
    N = int(data[1])
    A = list(map(int, data[2:2+M]))
    
    # Initialize the maximum slices as the number of pizzas (each pizza is 1 slice)
    max_slices = M
    
    # We can make up to N cuts in total
    # We want to maximize the number of slices, so we should make as many cuts as possible on the pizzas with the most cuts allowed
    # Sort the array A in descending order
    A.sort(reverse=True)
    
    # We have N cuts to distribute
    # For each pizza, we can make up to Ai cuts, and each cut increases the number of slices by 1
    # So, for each pizza, we can make min(Ai, remaining cuts) cuts
    # The number of slices for a pizza is 1 + number of cuts made on it
    remaining_cuts = N
    for i in range(M):
        if remaining_cuts <= 0:
            break
        # Maximum cuts we can make on this pizza
        max_cuts = min(A[i], remaining_cuts)
        # Increase the number of slices by max_cuts
        max_slices += max_cuts
        # Decrease remaining cuts
        remaining_cuts -= max_cuts
    
    print(max_slices)

if __name__ == '__main__':
    solve()