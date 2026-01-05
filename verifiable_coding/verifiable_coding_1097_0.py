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
        sinchan_area = 0
        
        # Process each friend
        for _ in range(N):
            # Determine the largest square that can be cut
            square_side = min(remaining_L, remaining_B)
            # The friend eats the square
            sinchan_area = max(sinchan_area, square_side * square_side)
            # Update the remaining cake
            if remaining_L > remaining_B:
                remaining_L -= square_side
            else:
                remaining_B -= square_side
        
        # Check if Sinchan gets to eat
        if sinchan_area > 0:
            results.append(f"Yes {sinchan_area}")
        else:
            results.append("No")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()