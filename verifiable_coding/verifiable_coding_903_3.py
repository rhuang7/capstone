import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        x1 = int(data[index])
        y1 = int(data[index+1])
        index += 2
        
        x2 = int(data[index])
        y2 = int(data[index+1])
        index += 2
        
        # The mirror should be placed at the point where the line from Kabir to Tara reflects off the x-axis
        # This is found by reflecting Tara's point over the x-axis and finding the intersection of the line
        # from Kabir to the reflected Tara with the x-axis
        # The reflected Tara's point is (x2, -y2)
        # The line from (x1, y1) to (x2, -y2) intersects the x-axis at (x, 0)
        # The x-coordinate of the intersection is given by the formula:
        # x = (x1 * (-y2) + x2 * y1) / (y1 + y2)
        x = (x1 * (-y2) + x2 * y1) / (y1 + y2)
        results.append(f"{x:.2f}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()