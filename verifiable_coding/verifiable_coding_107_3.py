import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        A = int(data[idx])
        B = int(data[idx+1])
        C = int(data[idx+2])
        D = int(data[idx+3])
        idx += 4
        
        # Determine possible boxes
        possible = [False]*4
        
        # Check if box 0 (first box) is possible
        # Box 0: fun values in (-infty, -1]
        # To end up in box 0, the final toy's fun value must be <= -1
        # The product of all fun values must be <= -1
        # Since each toy in box 0 has fun value <= -1, and others are in other ranges
        # We can consider the product of all fun values
        # The product will be negative if there are an odd number of negative values
        # But we need the final product to be <= -1
        # This depends on the number of toys in each box
        # We can consider the product of all fun values as a product of A terms <= -1, B terms in (-1,0), C terms in (0,1), D terms >=1
        # The product will be negative if there are an odd number of negative terms
        # The product's absolute value depends on the number of terms
        # We can use the following logic:
        # If the product of all fun values is <= -1, then box 0 is possible
        # But how to determine this based on the counts?
        # We can consider the following:
        # The product of all fun values is (product of A terms) * (product of B terms) * (product of C terms) * (product of D terms)
        # Since B terms are in (-1,0), their product is positive (as even number of negatives)
        # C terms are in (0,1), their product is between 0 and 1
        # D terms are >=1, their product is >=1
        # A terms are <= -1, their product is <= -1 (if A is odd) or >= -1 (if A is even)
        # So the overall product is (product of A terms) * (product of B terms) * (product of C terms) * (product of D terms)
        # We need this product to be <= -1
        # Let's consider the sign first:
        # The product is negative if there are an odd number of negative terms
        # The negative terms are A terms (<= -1) and B terms (in (-1,0))
        # So the number of negative terms is A + B
        # If A + B is odd, then the product is negative
        # If A + B is even, then the product is positive
        # So for box 0 to be possible, the product must be negative and <= -1
        # So A + B must be odd
        # Also, the product must be <= -1
        # Let's think of the product as follows:
        # The product of A terms is <= -1 (if A is odd) or >= -1 (if A is even)
        # The product of B terms is positive
        # The product of C terms is between 0 and 1
        # The product of D terms is >=1
        # So the overall product is (product of A terms) * (product of B terms) * (product of C terms) * (product of D terms)
        # For the product to be <= -1, the product of A terms must be negative and the product of B terms * C terms * D terms must be >= 1
        # But this is complex to compute directly
        # Instead, we can think of the product as:
        # If A is 0, then the product is positive
        # If A is odd, then the product is negative
        # So for box 0 to be possible, the product must be negative and <= -1
        # So A + B must be odd
        # And the product of A terms must be <= -1
        # But how to determine that?
        # We can use the following logic:
        # If A is 0, then the product is positive
        # If A is odd, then the product is negative
        # So for box 0 to be possible, A must be odd
        # And the product of A terms must be <= -1
        # But how?
        # We can think of the product of A terms as being <= -1 if A is odd
        # So if A is odd, then the product is negative
        # And the product of B terms is positive
        # The product of C terms is between 0 and 1
        # The product of D terms is >=1
        # So the overall product is (product of A terms) * (product of B terms) * (product of C terms) * (product of D terms)
        # For this to be <= -1, the product of A terms must be <= -1
        # So if A is odd, then the product is negative
        # So box 0 is possible if A is odd
        # But we also need to check if the product is <= -1
        # So box 0 is possible if A is odd and the product of all terms is <= -1
        # But how to compute that?
        # We can use the following logic:
        # The product of all terms is (product of A terms) * (product of B terms) * (product of C terms) * (product of D terms)
        # The product of A terms is <= -1 if A is odd
        # The product of B terms is positive
        # The product of C terms is between 0 and 1
        # The product of D terms is >=1
        # So the product of all terms is (product of A terms) * (product of B terms) * (product of C terms) * (product of D terms)
        # For this to be <= -1, the product of A terms must be <= -1
        # So box 0 is possible if A is odd
        # So possible[0] = (A % 2 == 1)
        # Similarly for other boxes
        # Box 1: fun values in (-1, 0)
        # The product must be in (-1, 0)
        # So the product must be negative and between -1 and 0
        # So the number of negative terms must be odd
        # And the product must be between -1 and 0
        # So possible[1] = (A + B) % 2 == 1 and (product of A terms * product of B terms * product of C terms * product of D terms) is between -1 and 0
        # But how to compute that?
        # We can use the following logic:
        # The product of all terms is (product of A terms) * (product of B terms) * (product of C terms) * (product of D terms)
        # The product of A terms is <= -1 if A is odd
        # The product of B terms is positive
        # The product of C terms is between 0 and 1
        # The product of D terms is >=1
        # So the product of all terms is (product of A terms) * (product of B terms) * (product of C terms) * (product of D terms)
        # For this to be between -1 and 0, the product of A terms must be negative and the product of B terms * C terms * D terms must be >= 1
        # So box 1 is possible if A is odd and (product of B terms * product of C terms * product of D terms) >= 1
        # But how to compute that?
        # We can use the following logic:
        # The product of B terms is positive
        # The product of C terms is between 0 and 1
        # The product of D terms is >=1
        # So the product of B terms * C terms * D terms is >= 0
        # So if A is odd, then the product of all terms is negative
        # So box 1 is possible if A is odd and (product of B terms * product of C terms * product of D terms) >= 1
        # But how to compute that?
        # We can use the following logic:
        # The product of B terms is positive
        # The product of C terms is between 0 and 1
        # The product of D terms is >=1
        # So the product of B terms * C terms * D terms is >= 0
        # So if A is odd, then the product of all terms is negative
        # So box 1 is possible if A is odd and (product of B terms * product of C terms * product of D terms) >= 1
        # But how to compute that?
        # We can use the following logic:
        # The product of B terms is positive
        # The product of C terms is between