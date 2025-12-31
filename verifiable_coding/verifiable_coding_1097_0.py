import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        L = int(data[idx])
        B = int(data[idx + 1])
        idx += 2
        # Initialize the cake dimensions
        remaining_L = L
        remaining_B = B
        # Track if Sinchan gets to eat
        sinchan_eats = True
        # Track the area Sinchan gets
        sinchan_area = 0
        # Process each friend
        for i in range(N):
            # Determine the largest square that can be cut
            square_side = min(remaining_L, remaining_B)
            # The friend eats the square
            if square_side == remaining_L:
                # The remaining part is (remaining_B - square_side) x remaining_L
                remaining_B -= square_side
            else:
                # The remaining part is (remaining_L - square_side) x remaining_B
                remaining_L -= square_side
            # Check if the cake is completely eaten
            if remaining_L == 0 and remaining_B == 0:
                break
        # Check if the cake is completely eaten
        if remaining_L == 0 and remaining_B == 0:
            # Sinchan gets to eat
            sinchan_area = remaining_L * remaining_B
            results.append(f"Yes {sinchan_area}")
        else:
            # Sinchan does not get to eat
            results.append("No")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()