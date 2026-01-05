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
        
        # The mirror should be placed at the point where the line segment between Kabir and Tara reflects off the x-axis
        # This is the x-coordinate of the reflection of Tara's position over the x-axis
        # The formula for the x-coordinate of the reflection is (2 * x2 - x1)
        mirror_x = (2 * x2 - x1)
        results.append(f"{mirror_x:.2f}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()