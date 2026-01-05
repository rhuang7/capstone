import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    D = int(input[0])
    X = int(input[1])
    Y = int(input[2])
    shifts = list(map(int, input[3:3+D]))
    
    total_earnings = 0
    
    for i in range(D):
        shift = shifts[i]
        # Minimum wage for the shift
        total_earnings += X
        # Tip calculation
        # Highest tip is Y for first shift, decreases by 2% per hour
        # So for shift i+1 (since shifts are 1-based), the tip is Y * (1 - 0.02 * (shift - 1))
        tip = Y * (1 - 0.02 * (shift - 1))
        total_earnings += tip
    
    if total_earnings >= 300:
        print("YES")
    else:
        print("NO")