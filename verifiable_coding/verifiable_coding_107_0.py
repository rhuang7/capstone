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
        
        # Check if the final toy can be in each box
        possible = [False] * 4
        
        # Check for first box: [-inf, -1]
        # The final toy must be <= -1
        # The product of all toys must be <= -1
        # Since the product is the product of all toys, which is the product of A, B, C, D terms
        # But since we don't know the actual values, we need to find if it's possible to have the product <= -1
        # For this, we can consider the sign of the product
        # The product is negative if there are an odd number of negative terms
        # But since the boxes are defined by ranges, we need to find if it's possible for the product to be in the desired range
        
        # For the first box, the final toy must be <= -1
        # This is possible if the product is negative and has absolute value >= 1
        # So, check if the product can be negative and have absolute value >= 1
        # For this, we need to have an odd number of negative terms and the product's absolute value >= 1
        # But since we don't know the actual values, we need to check if it's possible
        
        # For the first box, possible if the product is negative and absolute value >= 1
        # This can be achieved if there is at least one toy in the first box (A >= 1) and at least one in the fourth box (D >= 1)
        # Because the first box has negative values and the fourth has positive values
        # So, if A >= 1 and D >= 1, then the product can be negative and have absolute value >= 1
        # So possible[0] = (A >= 1 and D >= 1)
        possible[0] = (A >= 1 and D >= 1)
        
        # Check for second box: (-1, 0)
        # The final toy must be between -1 and 0
        # This is possible if the product is negative and absolute value < 1
        # So, check if it's possible to have the product negative and absolute value < 1
        # This can be achieved if there is at least one toy in the first box (A >= 1) and at least one in the second box (B >= 1)
        # Because the first box has negative values and the second has values between -1 and 0
        # So, possible[1] = (A >= 1 and B >= 1)
        possible[1] = (A >= 1 and B >= 1)
        
        # Check for third box: (0, 1)
        # The final toy must be between 0 and 1
        # This is possible if the product is positive and absolute value < 1
        # So, check if it's possible to have the product positive and absolute value < 1
        # This can be achieved if there is at least one toy in the second box (B >= 1) and at least one in the third box (C >= 1)
        # Because the second box has values between -1 and 0 and the third has values between 0 and 1
        # So, possible[2] = (B >= 1 and C >= 1)
        possible[2] = (B >= 1 and C >= 1)
        
        # Check for fourth box: [1, inf)
        # The final toy must be >= 1
        # This is possible if the product is positive and absolute value >= 1
        # So, check if it's possible to have the product positive and absolute value >= 1
        # This can be achieved if there is at least one toy in the fourth box (D >= 1) and at least one in the third box (C >= 1)
        # Because the fourth box has positive values and the third has values between 0 and 1
        # So, possible[3] = (D >= 1 and C >= 1)
        possible[3] = (D >= 1 and C >= 1)
        
        # Convert to "Ya" or "Tidak"
        res = []
        for p in possible:
            res.append("Ya" if p else "Tidak")
        results.append(" ".join(res))
    
    print("\n".join(results))