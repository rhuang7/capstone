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
        # This is the x-coordinate of the intersection of the line from Kabir to Tara's reflection across the x-axis
        # The reflection of Tara's point across the x-axis is (x2, -y2)
        # The line from Kabir (x1, y1) to Tara's reflection (x2, -y2) intersects the x-axis at the mirror position
        # The x-coordinate of the intersection is calculated as (x1 * (-y2) + x2 * y1) / (y1 + y2)
        x_mirror = (x1 * (-y2) + x2 * y1) / (y1 + y2)
        print("{0:.2f}".format(x_mirror))
        
if __name__ == '__main__':
    solve()