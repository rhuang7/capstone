import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        a1, b1 = data[index], data[index+1]
        a2, b2 = data[index+2], data[index+3]
        index += 4
        
        a1 = int(a1)
        b1 = int(b1)
        a2 = int(a2)
        b2 = int(b2)
        
        # Check if the two rectangles can form a square
        # The total area of the two rectangles must be a perfect square
        total_area = a1 * b1 + a2 * b2
        is_perfect_square = int(total_area**0.5) ** 2 == total_area
        
        if not is_perfect_square:
            results.append("NO")
            continue
        
        # Check if the rectangles can be arranged to form a square
        # The sum of one side of the rectangles must equal the side of the square
        # And the other sides must be equal
        side = int(total_area**0.5)
        
        # Check possible combinations
        # Case 1: a1 + a2 == side and b1 == b2
        if (a1 + a2 == side and b1 == b2) or (a1 + a2 == side and b1 == b2):
            results.append("YES")
        # Case 2: a1 + b2 == side and a2 == b1
        elif (a1 + b2 == side and a2 == b1) or (a1 + b2 == side and a2 == b1):
            results.append("YES")
        # Case 3: b1 + b2 == side and a1 == a2
        elif (b1 + b2 == side and a1 == a2) or (b1 + b2 == side and a1 == a2):
            results.append("YES")
        # Case 4: b1 + a2 == side and a1 == b2
        elif (b1 + a2 == side and a1 == b2) or (b1 + a2 == side and a1 == b2):
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()