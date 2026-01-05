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
        # This is the x-coordinate of the intersection of the line from (x1, y1) to (x2, -y2) with the x-axis
        # The x-coordinate is the same for both points on the line
        # So we find the x-coordinate of the line passing through (x1, y1) and (x2, -y2)
        # The line equation is (y - y1) = ((-y2 - y1)/(x2 - x1))(x - x1)
        # Setting y = 0, we solve for x
        if x1 == x2:
            # Vertical line, mirror is at x1
            x_mirror = x1
        else:
            # Calculate x-coordinate of the mirror
            x_mirror = (x1 * (-y2) + x2 * y1) / (y1 - y2)
        
        # Print with 2 decimal places
        print(f"{x_mirror:.2f}")

if __name__ == '__main__':
    solve()