import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        L = int(input[idx])
        B = int(input[idx + 1])
        idx += 2
        # Initialize the cake dimensions
        remaining_L = L
        remaining_B = B
        # Track if Sinchan gets to eat
        sinchan_eats = False
        # Track the area Sinchan gets
        sinchan_area = 0
        # Process each friend
        for i in range(N):
            # Determine the largest square that can be cut
            square_side = min(remaining_L, remaining_B)
            # The friend eats the square
            eaten_area = square_side * square_side
            # The remaining part is a rectangle
            if remaining_L > remaining_B:
                remaining_L -= square_side
            else:
                remaining_B -= square_side
            # Check if the remaining area is zero
            if remaining_L == 0 or remaining_B == 0:
                break
        # Check if the cake is completely eaten or not
        if remaining_L == 0 or remaining_B == 0:
            # Check if Sinchan gets to eat
            if (N % 2 == 1):
                sinchan_eats = True
                sinchan_area = remaining_L * remaining_B
        else:
            # If there is still cake left, Sinchan cannot eat
            sinchan_eats = False
        if sinchan_eats:
            results.append(f"Yes {sinchan_area}")
        else:
            results.append("No")
    print("\n".join(results))

if __name__ == '__main__':
    solve()