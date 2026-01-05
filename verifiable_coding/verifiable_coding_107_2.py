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
        
        possible = [False] * 4
        
        # Check if the final toy can be in box 1 (<= -1)
        # The product of all toys must be <= -1
        # Since each toy in box 1 is <= -1, box 2 is between -1 and 0, box 3 is between 0 and 1, box 4 is >= 1
        # The product of all toys is the product of all fun values
        # We need to find if there exists a way to combine the toys such that the final product is <= -1
        
        # For box 1 to be possible, the product of all toys must be <= -1
        # Let's consider the sign of the product
        # The number of negative toys is A + B (since box 1 and box 2 have negative values)
        # The number of positive toys is C + D (since box 3 and box 4 have positive values)
        
        # If the number of negative toys is even, the product is positive
        # If odd, the product is negative
        # So for the product to be <= -1, the number of negative toys must be odd
        
        # Also, the product must have absolute value >= 1
        # The absolute value of the product is the product of the absolute values of all toys
        # We need to check if the product of absolute values of all toys is >= 1
        
        # The product of absolute values is:
        # (product of absolute values of box 1 toys) * (product of absolute values of box 2 toys) * (product of absolute values of box 3 toys) * (product of absolute values of box 4 toys)
        # Since box 1 toys are <= -1, their absolute values are >= 1
        # Box 2 toys are between -1 and 0, their absolute values are between 0 and 1
        # Box 3 toys are between 0 and 1, their absolute values are between 0 and 1
        # Box 4 toys are >= 1, their absolute values are >= 1
        
        # So the product of absolute values is >= 1 only if there are enough toys in box 1 and box 4 to make the product >= 1
        
        # Let's check if the product of absolute values is >= 1
        # We can approximate it by considering that box 1 and box 4 contribute at least 1 each, and box 2 and box 3 contribute at most 1 each
        # So if A + D >= 1, then the product of absolute values is >= 1
        
        # But this is not sufficient, we need to check if there is a way to combine the toys such that the final product is <= -1
        
        # For box 1 to be possible:
        # 1. The number of negative toys must be odd
        # 2. The product of absolute values of all toys must be >= 1
        
        # Let's check these conditions
        num_neg = A + B
        num_pos = C + D
        if num_neg % 2 == 1:
            if (A + D) >= 1:
                possible[0] = True
        
        # Check if box 2 can be the special box
        # The product must be in (-1, 0)
        # So the product must be negative and between -1 and 0
        # For this to happen, the number of negative toys must be odd
        # And the product of absolute values must be < 1
        
        # The product of absolute values is < 1 only if there are not enough toys in box 1 and box 4 to make the product >= 1
        # So if (A + D) < 1, then the product of absolute values is < 1
        
        if num_neg % 2 == 1:
            if (A + D) < 1:
                possible[1] = True
        
        # Check if box 3 can be the special box
        # The product must be in (0, 1)
        # So the product must be positive and between 0 and 1
        # For this to happen, the number of negative toys must be even
        # And the product of absolute values must be < 1
        
        if num_neg % 2 == 0:
            if (A + D) < 1:
                possible[2] = True
        
        # Check if box 4 can be the special box
        # The product must be >= 1
        # So the product must be positive and >= 1
        # For this to happen, the number of negative toys must be even
        # And the product of absolute values must be >= 1
        
        if num_neg % 2 == 0:
            if (A + D) >= 1:
                possible[3] = True
        
        # Now, we need to check if there are any toys
        if A + B + C + D == 0:
            # No toys, but the problem says that the sum is > 0
            pass
        
        # Convert to "Ya" or "Tidak"
        res = []
        for p in possible:
            res.append("Ya" if p else "Tidak")
        results.append(" ".join(res))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()