import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    M = int(data[0])
    N = int(data[1])
    A = list(map(int, data[2:2+M]))
    
    # Initialize the maximum slices as M (no cuts)
    max_slices = M
    
    # We can make up to N cuts in total
    # We want to maximize the number of slices, so we should cut the pizzas that give the most additional slices per cut
    # The maximum additional slices for a pizza with Ai cuts is Ai (since each cut adds at most 1 slice)
    # So we sort the array A in descending order and apply cuts to the largest Ai first
    
    # Sort A in descending order
    A.sort(reverse=True)
    
    # Apply cuts to the largest Ai first
    for i in range(min(N, len(A))):
        # Each cut adds 1 slice, so we can make up to Ai cuts on this pizza
        # But we have N cuts to distribute
        cuts = min(N, A[i])
        max_slices += cuts
        N -= cuts
        if N == 0:
            break
    
    print(max_slices)

if __name__ == '__main__':
    solve()