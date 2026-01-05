import sys

def solve():
    import sys
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
        
        # Calculate the number of times each group comes
        cnt_x = N // x
        cnt_y = N // y
        cnt_z = N // z
        
        # The number of times all three come is the minimum of the counts
        # But we need to find the number of days when all three come
        # So we need to find the LCM of x, y, z and count how many multiples of LCM are there in N days
        from math import gcd
        
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        lcm_xy = lcm(x, y)
        lcm_xyz = lcm(lcm_xy, z)
        
        # Number of times all three come
        result = N // lcm_xyz
        
        print(result)

if __name__ == '__main__':
    solve()