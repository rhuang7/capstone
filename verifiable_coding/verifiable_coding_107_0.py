import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        A = int(data[index])
        B = int(data[index+1])
        C = int(data[index+2])
        D = int(data[index+3])
        index += 4
        
        # Determine possible special boxes
        possible = [False] * 4
        
        # Check if box 0 (first box) is possible
        # Box 0: fun values in (-infty, -1]
        # The product of all toys' fun values must be <= -1
        # Since all toys in box 0 are <= -1, and others are in (-1, 0), (0, 1), [1, inf)
        # The product will be negative if there is an odd number of negative values
        # But we need to check if the final product can be <= -1
        # We can check if the total number of toys is odd
        total = A + B + C + D
        if total % 2 == 1:
            possible[0] = True
        
        # Check if box 1 (second box) is possible
        # Box 1: fun values in (-1, 0)
        # The product of all toys' fun values must be in (-1, 0)
        # This is possible if the total number of toys is even and the product is negative
        # But we need to check if the final product can be in (-1, 0)
        # We can check if the total number of toys is even and there is at least one toy in box 1
        if total % 2 == 0 and B > 0:
            possible[1] = True
        
        # Check if box 2 (third box) is possible
        # Box 2: fun values in (0, 1)
        # The product of all toys' fun values must be in (0, 1)
        # This is possible if the total number of toys is even and the product is positive
        # But we need to check if the final product can be in (0, 1)
        # We can check if the total number of toys is even and there is at least one toy in box 2
        if total % 2 == 0 and C > 0:
            possible[2] = True
        
        # Check if box 3 (fourth box) is possible
        # Box 3: fun values in [1, inf)
        # The product of all toys' fun values must be >= 1
        # This is possible if the total number of toys is odd and there is at least one toy in box 3
        if total % 2 == 1 and D > 0:
            possible[3] = True
        
        # Convert to "Ya" or "Tidak"
        res = []
        for p in possible:
            res.append("Ya" if p else "Tidak")
        results.append(" ".join(res))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()