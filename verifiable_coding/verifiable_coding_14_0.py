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
        is_square = int(total_area**0.5) ** 2 == total_area
        
        # Check if the sides can be arranged to form a square
        # The sum of one side of each rectangle must be equal to the other side of each rectangle
        # Try all possible combinations of sides
        sides = [(a1, b1), (a2, b2), (b1, a1), (b2, a2)]
        found = False
        for s1 in sides:
            for s2 in sides:
                if s1[0] == s2[1] and s1[1] == s2[0]:
                    found = True
                    break
            if found:
                break
        
        if is_square and found:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()