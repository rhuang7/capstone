import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        a = int(data[index+2])
        b = int(data[index+3])
        index += 4
        
        # The rabbits meet when (x + a * t) == (y - b * t)
        # Solving for t: t = (y - x) / (a + b)
        # Check if (y - x) is divisible by (a + b) and if t is non-negative
        distance = y - x
        speed_sum = a + b
        
        if distance % speed_sum != 0:
            print(-1)
        else:
            t_val = distance // speed_sum
            print(t_val)
            
if __name__ == '__main__':
    solve()