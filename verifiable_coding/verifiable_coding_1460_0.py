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
        # Tip starts at Y for the first shift, decreases by 2% per hour
        # Each day, the tip decreases by 2% for each subsequent shift
        # So for the i-th day, the tip starts at Y * (1 - 0.02 * (i))
        # But since the tip decreases by 2% per hour, and the shift is 1 hour,
        # the tip decreases by 2% for each day after the first day
        # So for the i-th day, the tip is Y * (1 - 0.02 * i)
        tip = Y * (1 - 0.02 * i)
        total_earnings += tip * shift
    
    if total_earnings >= 300:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()