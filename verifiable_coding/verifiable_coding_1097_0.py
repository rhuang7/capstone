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
        l, b = L, B
        # Track if Sinchan gets to eat
        sinchan_eats = True
        # Track the remaining area
        remaining_area = l * b
        # Track if the cake is already a square
        is_square = (l == b)
        # Process each friend
        for i in range(N):
            if is_square:
                # If cake is a square, the friend takes the whole cake
                remaining_area = 0
                sinchan_eats = False
                break
            # Determine the largest square that can be cut
            square_side = min(l, b)
            # The friend takes the square
            taken_area = square_side * square_side
            remaining_area -= taken_area
            # Update the cake dimensions
            if l > b:
                l = l - square_side
            else:
                b = b - square_side
            # Check if the cake is now a square
            is_square = (l == b)
        # Check if the cake is completely eaten
        if remaining_area == 0:
            sinchan_eats = False
        # Determine the output
        if sinchan_eats:
            results.append(f"Yes {remaining_area}")
        else:
            results.append("No")
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()