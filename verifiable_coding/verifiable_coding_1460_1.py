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
        # The tip starts at Y for the first shift, decreases by 2% per hour
        # Each day, the tip decreases by 2% for each subsequent shift
        # So for the i-th day, the tip starts at Y * (1 - 0.02 * (i))
        # But since the shift number is given, we need to calculate the tip based on the shift number
        # The tip decreases by 2% per hour, so for the shift number, it's Y * (1 - 0.02 * (shift - 1))
        tip = Y * (1 - 0.02 * (shift - 1))
        total_earnings += tip
    
    if total_earnings >= 300:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()