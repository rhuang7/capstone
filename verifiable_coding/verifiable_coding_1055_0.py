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
    
    # Sort pizzas by the maximum cuts they can take (Ai) in descending order
    A.sort(reverse=True)
    
    for i in range(M):
        # Maximum cuts we can make on this pizza
        max_cuts = min(remaining_cuts, A[i])
        # Each cut increases the number of slices by 1
        total_slices += max_cuts
        remaining_cuts -= max_cuts
        if remaining_cuts == 0:
            break
    
    print(total_slices)

if __name__ == '__main__':
    solve()