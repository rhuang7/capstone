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
        current_L = L
        current_B = B
        remaining_area = current_L * current_B
        sinchan_area = 0
        friends_remaining = N
        
        while friends_remaining > 0 and remaining_area > 0:
            # Determine the largest square that can be cut
            square_side = min(current_L, current_B)
            square_area = square_side * square_side
            remaining_area -= square_area
            friends_remaining -= 1
            
            # Update the cake dimensions after cutting the square
            if current_L > current_B:
                current_L = current_L - square_side
            else:
                current_B = current_B - square_side
        
        if friends_remaining == 0 or remaining_area == 0:
            results.append("No")
        else:
            results.append(f"Yes {remaining_area}")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()