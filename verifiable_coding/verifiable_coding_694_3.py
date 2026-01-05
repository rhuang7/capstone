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
        
        # Compute the number of times each group comes in N days
        cnt_x = N // x
        cnt_y = N // y
        cnt_z = N // z
        
        # The number of times all three groups come on the same day is the minimum of the counts
        # But we need to count the number of days when all three come, which is the number of days when the LCM of x, y, z divides the day number
        # So we compute the LCM of x, y, z and then count how many multiples of LCM are there in N days
        lcm_xy = x * y // math.gcd(x, y)
        lcm_xyz = lcm_xy * z // math.gcd(lcm_xy, z)
        
        result = N // lcm_xyz
        print(result)

if __name__ == '__main__':
    solve()