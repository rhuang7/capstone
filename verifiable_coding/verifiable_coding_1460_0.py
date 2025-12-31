import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    D = int(data[0])
    X = int(data[1])
    Y = int(data[2])
    
    shifts = list(map(int, data[3:3+D]))
    
    total_earnings = 0
    
    for i in range(D):
        shift = shifts[i]
        # Minimum wage for the shift
        total_earnings += X
        # Tip calculation
        # Highest tip is Y for first shift, decreases by 2% per hour
        # So for shift j (starting from 1), tip is Y * (1 - 0.02 * (j-1))
        tip = Y * (1 - 0.02 * (shift - 1))
        total_earnings += tip
    
    if total_earnings >= 300:
        print("YES")
    else:
        print("NO")