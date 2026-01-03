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
        
        # The number of times all three come on the same day is the minimum of the counts
        # But we need to count the number of days when all three come
        # So we need to find the number of days when all three come
        # Which is the number of days that are multiples of LCM(x, y, z)
        # But since we need to count the number of days in N days when all three come
        # We can use inclusion-exclusion principle
        
        # LCM of x, y, z
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        lcm_xy = lcm(x, y)
        lcm_xyz = lcm(lcm_xy, z)
        
        # Number of days when all three come
        total = N // lcm_xyz
        
        print(total)

if __name__ == '__main__':
    solve()