import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        x1 = int(data[index])
        y1 = int(data[index+1])
        index += 2
        
        x2 = int(data[index])
        y2 = int(data[index+1])
        index += 2
        
        # The mirror should be placed at the x-coordinate where the line from Kabir to Tara reflects off the x-axis
        # This is the x-coordinate of the intersection of the line from Kabir to Tara with the x-axis
        # The formula is: x = (x1 * y2 - x2 * y1) / (y1 + y2)
        x_mirror = (x1 * y2 - x2 * y1) / (y1 + y2)
        print(f"{x_mirror:.2f}")

if __name__ == '__main__':
    solve()