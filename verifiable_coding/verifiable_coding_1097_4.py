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
        # Track if Sinchan gets to eat
        sinchan_gets = False
        # Track the area Sinchan gets
        sinchan_area = 0
        
        for i in range(N):
            # Determine the largest square
            square_side = min(current_L, current_B)
            # The square is eaten by the friend
            if current_L == square_side:
                # Remaining part is (current_L - square_side) x current_B
                current_L = current_L - square_side
            else:
                # Remaining part is current_L x (current_B - square_side)
                current_B = current_B - square_side
            # Check if the cake is completely eaten
            if current_L == 0 and current_B == 0:
                break
            # Check if the next friend can eat
            if current_L == 0 or current_B == 0:
                sinchan_gets = True
                sinchan_area = current_L * current_B
                break
        
        if sinchan_gets:
            results.append(f"Yes {sinchan_area}")
        else:
            results.append("No")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()