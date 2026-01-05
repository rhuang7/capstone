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
        base_wage = X
        tip = Y * (1 - 0.02 * (shift - 1))
        total_earnings += base_wage + tip
    
    if total_earnings >= 300:
        print("YES")
    else:
        print("NO")