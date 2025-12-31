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
        
        # Calculate the number of times each group comes in N days
        cnt_x = N // x
        cnt_y = N // y
        cnt_z = N // z
        
        # The number of times all three groups come on the same day
        # is the number of days that are multiples of LCM(x, y, z)
        lcm_xy = x * y // math.gcd(x, y)
        lcm_xyz = lcm_xy * z // math.gcd(lcm_xy, z)
        cnt_all = N // lcm_xyz
        
        print(cnt_all)

if __name__ == '__main__':
    solve()