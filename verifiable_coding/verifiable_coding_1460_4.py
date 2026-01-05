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
        # Minimum wage is X per shift
        total_earnings += X
        
        # Tip starts at Y for the first shift, decreases by 2% per hour
        # The tip for the i-th day is Y * (1 - 0.02 * (shift - 1))
        tip = Y * (1 - 0.02 * (shift - 1))
        total_earnings += tip
    
    if total_earnings >= 300:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()