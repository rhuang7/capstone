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
        # connecting Kabir and Tara's reflection on the x-axis intersects the x-axis.
        # The reflection of Tara is (x2, -y2), so the line from Kabir to Tara's reflection
        # is (x1, y1) to (x2, -y2). The intersection with the x-axis (y=0) is the mirror position.
        
        # Using the formula for the x-intercept of a line through two points:
        # x = (x1 * (-y2) - x2 * y1) / ( -y2 - y1 )
        # Simplify: x = (x1 * y2 + x2 * y1) / (y1 + y2)
        x_mirror = (x1 * y2 + x2 * y1) / (y1 + y2)
        
        print(f"{x_mirror:.2f}")

if __name__ == '__main__':
    solve()