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
        is_square = False
        side = int(total_area ** 0.5)
        if side * side == total_area:
            is_square = True
        
        # Check if the rectangles can be arranged to form a square
        # The sum of one side of each rectangle must equal the side of the square
        # And the other sides must be equal
        if is_square:
            # Check if one rectangle's side matches the square's side
            # and the other rectangle's side matches the square's side
            if (a1 == side and b1 == side) or (a1 == side and b2 == side) or (b1 == side and a2 == side) or (b1 == side and b2 == side):
                results.append("YES")
            else:
                results.append("NO")
        else:
            results.append("NO")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()