import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
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
        for i in range(1, int(total_area**0.5) + 1):
            if i * i == total_area:
                is_square = True
                break
        
        # Check if the rectangles can be arranged to form a square
        # The sum of one side of the rectangles must equal the side of the square
        # And the other sides must be equal
        square_side = int(total_area**0.5)
        possible = False
        # Try all combinations of sides
        for a, b in [(a1, b1), (b1, a1), (a2, b2), (b2, a2)]:
            if a == square_side and b == square_side:
                possible = True
                break
            if a == square_side and b == square_side:
                possible = True
                break
            if a == square_side and b == square_side:
                possible = True
                break
            if a == square_side and b == square_side:
                possible = True
                break
        
        if is_square and possible:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()