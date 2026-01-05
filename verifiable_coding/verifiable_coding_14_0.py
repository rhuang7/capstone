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
        
        # Check if the two rectangles can be arranged to form a square
        # Either (a1 + a2) == b1 == b2 or (b1 + b2) == a1 == a2
        # Or (a1 == a2 and b1 + b2 == a1) or (b1 == b2 and a1 + a2 == b1)
        if is_square:
            # Check if the two rectangles can be arranged to form a square
            if (a1 + a2 == b1 and b1 == b2) or (b1 + b2 == a1 and a1 == a2):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")

if __name__ == '__main__':
    solve()