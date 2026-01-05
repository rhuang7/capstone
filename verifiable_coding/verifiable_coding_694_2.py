import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        index += 3
        
        # Calculate LCM of x, y, z
        lcm_xy = x * y // math.gcd(x, y)
        lcm_xyz = lcm_xy * z // math.gcd(lcm_xy, z)
        
        # Number of times all three come on the same day in N days
        count = N // lcm_xyz
        
        print(count)

if __name__ == '__main__':
    solve()