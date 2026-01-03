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
        
        # Determine possible boxes
        possible = [False] * 4
        
        # Check if box 0 (first box) is possible
        # The product of all toys' fun values must be <= -1
        # Since each toy in first box is <= -1, second box is between -1 and 0, third between 0 and 1, fourth >= 1
        # The product of all toys' fun values is the product of A values <= -1, B values between -1 and 0, C values between 0 and 1, D values >= 1
        # The product will be <= -1 if there are an odd number of negative values and the product of absolute values is >= 1
        # But since we don't know the actual values, we need to check if it's possible to have the final product <= -1
        # For box 0 to be possible, the product of all toys must be <= -1
        # The product of all toys is (product of A toys) * (product of B toys) * (product of C toys) * (product of D toys)
        # Since B toys are between -1 and 0, their product is between -1 and 0
        # C toys are between 0 and 1, their product is between 0 and 1
        # D toys are >= 1, their product is >= 1
        # A toys are <= -1, their product is <= -1
        # So the total product is (product of A) * (product of B) * (product of C) * (product of D)
        # We need to check if it's possible for this product to be <= -1
        # The product of B is between -1 and 0, so it's negative
        # The product of C is between 0 and 1, so it's positive
        # The product of D is >= 1, so it's positive
        # The product of A is <= -1, so it's negative
        # So the total product is (negative) * (negative) * (positive) * (positive) = positive
        # So it's impossible for the product to be <= -1
        # Therefore, box 0 is not possible
        possible[0] = False
        
        # Check if box 1 (second box) is possible
        # The product of all toys must be in (-1, 0)
        # The product is (product of A) * (product of B) * (product of C) * (product of D)
        # A is <= -1, B is between -1 and 0, C is between 0 and 1, D is >= 1
        # The product of A is <= -1, product of B is between -1 and 0, product of C is between 0 and 1, product of D is >= 1
        # So the product is (negative) * (negative) * (positive) * (positive) = positive
        # So it's impossible for the product to be in (-1, 0)
        # Therefore, box 1 is not possible
        possible[1] = False
        
        # Check if box 2 (third box) is possible
        # The product of all toys must be in (0, 1)
        # The product is (product of A) * (product of B) * (product of C) * (product of D)
        # A is <= -1, B is between -1 and 0, C is between 0 and 1, D is >= 1
        # The product of A is <= -1, product of B is between -1 and 0, product of C is between 0 and 1, product of D is >= 1
        # So the product is (negative) * (negative) * (positive) * (positive) = positive
        # So it's impossible for the product to be in (0, 1)
        # Therefore, box 2 is not possible
        possible[2] = False
        
        # Check if box 3 (fourth box) is possible
        # The product of all toys must be >= 1
        # The product is (product of A) * (product of B) * (product of C) * (product of D)
        # A is <= -1, B is between -1 and 0, C is between 0 and 1, D is >= 1
        # The product of A is <= -1, product of B is between -1 and 0, product of C is between 0 and 1, product of D is >= 1
        # So the product is (negative) * (negative) * (positive) * (positive) = positive
        # So it's possible for the product to be >= 1
        # Therefore, box 3 is possible
        possible[3] = True
        
        # Now, check if the total number of toys is 1
        total = A + B + C + D
        if total == 1:
            # Only one toy, so it's already in the special box
            # So the possible boxes are the box of that toy
            # The toy is in box 0 if it's <= -1, box 1 if it's in (-1, 0), box 2 if it's in (0, 1), box 3 if it's >= 1
            # So we need to check which box is possible
            # For example, if there is 1 toy in box 0, then it's possible for box 0 to be the special box
            # So we need to check which boxes have at least one toy
            # So if A >= 1, then box 0 is possible
            # If B >= 1, then box 1 is possible
            # If C >= 1, then box 2 is possible
            # If D >= 1, then box 3 is possible
            # So we need to check which of these are true
            # But we also need to make sure that the total is 1
            # So we need to set possible to True for the boxes that have at least one toy
            # But we also need to make sure that the total is 1
            # So if A == 1, then possible[0] = True
            # If B == 1, then possible[1] = True
            # If C == 1, then possible[2] = True
            # If D == 1, then possible[3] = True
            # But we also need to check if the total is 1
            # So if total == 1, then the possible boxes are the ones that have at least one toy
            # So we need to check which of A, B, C, D is >= 1
            # So we need to set possible[0] = (A >= 1)
            # possible[1] = (B >= 1)
            # possible[2] = (C >= 1)
            # possible[3] = (D >= 1)
            # But we also need to check if the total is 1
            # So if total == 1, then the possible boxes are the ones that have at least one toy
            # So we need to set possible to True for those boxes
            # So we need to check which boxes have at least one toy
            # So possible[0] = (A >= 1)
            # possible[1] = (B >= 1)
            # possible[2] = (C >= 1)
            # possible[3] = (D >= 1)
            # But we also need to make sure that the total is 1
            # So we need to set possible to True for those boxes
            # So we need to check which boxes have at least one toy
            # So possible[0] = (A >= 1)
            # possible[1] = (B >= 1)
            # possible[2] = (C >= 1)
            # possible[3] = (D >= 1)
            # But we also need to check if the total is 1
            # So if total == 1, then the possible boxes are the ones that have at least one toy
            # So we need to set possible to True for those boxes
            # So we need to check which boxes have at least one toy
            # So possible[0] = (A >= 1)
            # possible[1] = (B >= 1)
            # possible[2] = (C >= 1)
            # possible[3] = (D >= 1)
            # But we also need to make sure that the total is 1
            # So we need to set possible to True for