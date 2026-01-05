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
        # => a*t + b*t = y - x
        # => t*(a + b) = y - x
        # => t = (y - x) / (a + b)
        # Check if (y - x) is divisible by (a + b)
        distance = y - x
        speed_sum = a + b
        
        if speed_sum == 0:
            print(-1)
            continue
        
        if distance % speed_sum == 0:
            print(distance // speed_sum)
        else:
            print(-1)

if __name__ == '__main__':
    solve()