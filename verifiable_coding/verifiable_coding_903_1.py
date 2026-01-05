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
        
        # The mirror should be placed at the x-coordinate where the line
        # from Kabir to Tara's reflection (across the x-axis) intersects the x-axis.
        # The reflection of Tara's point (x2, y2) is (x2, -y2)
        # The line from (x1, y1) to (x2, -y2) intersects the x-axis at the mirror position.
        
        # Equation of the line: (y - y1) = m(x - x1), where m = (y2 + y1)/(x2 - x1)
        # Set y = 0 and solve for x.
        if x1 == x2:
            # Vertical line, mirror is at x1
            x_mirror = x1
        else:
            m = (y2 + y1) / (x2 - x1)
            x_mirror = x1 - (y1 * (x2 - x1)) / (y2 + y1)
        
        print(f"{x_mirror:.2f}")

if __name__ == '__main__':
    solve()