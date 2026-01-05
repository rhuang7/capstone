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
        
        # The distance between the rabbits initially
        distance = y - x
        
        # The relative speed at which the distance decreases
        # Taller rabbit moves right (a), shorter moves left (b)
        # So the distance decreases by (a + b) per second
        if a + b == 0:
            print(-1)
            continue
        
        # Check if the distance can be covered with the relative speed
        if distance % (a + b) != 0:
            print(-1)
        else:
            time = distance // (a + b)
            print(time)

if __name__ == '__main__':
    solve()