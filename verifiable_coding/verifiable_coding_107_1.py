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
        
        # Check for box 0 (first box: [-inf, -1])
        # The product must be <= -1
        # The product of all toys is the product of all fun values
        # Since each toy is in a specific box, we can determine the sign and magnitude
        # We need to check if it's possible for the final product to be <= -1
        # The product of all toys is the product of A toys <= -1, B toys in (-1, 0), C toys in (0, 1), D toys >= 1
        # We can think of it as:
        # sign = (-1)^A * (-1)^B * 1^C * 1^D = (-1)^(A+B)
        # magnitude = (product of A toys) * (product of B toys) * (product of C toys) * (product of D toys)
        # For the product to be <= -1, the magnitude must be >= 1 and the sign must be negative
        # So, we need:
        # 1. sign is negative: A + B is odd
        # 2. magnitude >= 1
        # For magnitude >= 1, we need:
        # A toys <= -1: each contributes a value <= -1
        # B toys in (-1, 0): each contributes a value between -1 and 0
        # C toys in (0, 1): each contributes a value between 0 and 1
        # D toys >= 1: each contributes a value >= 1
        # The product of A toys is <= (-1)^A
        # The product of B toys is in (-1, 0)
        # The product of C toys is in (0, 1)
        # The product of D toys is >= 1
        # So the product of all toys is:
        # (product of A toys) * (product of B toys) * (product of C toys) * (product of D toys)
        # To have magnitude >= 1, we need:
        # (product of A toys) * (product of D toys) >= 1
        # (product of B toys) * (product of C toys) <= 1
        # For the product of A toys, since each is <= -1, the product is <= (-1)^A
        # For the product of D toys, since each is >= 1, the product is >= 1^D = 1
        # So (product of A toys) * (product of D toys) <= (-1)^A * (product of D toys)
        # For this to be >= 1, we need:
        # (-1)^A * (product of D toys) >= 1
        # Since product of D toys >= 1, this is possible only if A is even
        # Because if A is even, (-1)^A is 1, and product of D toys >= 1, so the product is >= 1
        # If A is odd, (-1)^A is -1, and product of D toys >= 1, so the product is <= -1
        # So for (product of A toys) * (product of D toys) >= 1, we need A even
        # For (product of B toys) * (product of C toys) <= 1
        # product of B toys is in (-1, 0), product of C toys is in (0, 1)
        # So their product is in (-1, 0) * (0, 1) = (-1, 0)
        # So it is always <= 1
        # So the condition is satisfied
        # So for box 0 to be possible, we need A even and A + B is odd
        if A % 2 == 0 and (A + B) % 2 == 1:
            possible[0] = True
        
        # Check for box 1 (second box: (-1, 0))
        # The product must be in (-1, 0)
        # The sign is negative
        # The magnitude must be < 1
        # So the product must be in (-1, 0)
        # For this, the sign must be negative (A + B is odd)
        # And the magnitude must be < 1
        # The magnitude is the product of all toys' absolute values
        # For the magnitude to be < 1, we need:
        # (product of A toys' absolute values) * (product of B toys' absolute values) * (product of C toys' absolute values) * (product of D toys' absolute values) < 1
        # product of A toys' absolute values is >= 1^A = 1
        # product of B toys' absolute values is in (0, 1)^B
        # product of C toys' absolute values is in (0, 1)^C
        # product of D toys' absolute values is >= 1^D = 1
        # So the product is >= 1 * (product of B toys' absolute values) * (product of C toys' absolute values) * 1
        # For this to be < 1, we need:
        # (product of B toys' absolute values) * (product of C toys' absolute values) < 1
        # Since B and C are in (-1, 0) and (0, 1), their product is in (-1, 0) * (0, 1) = (-1, 0)
        # So their product is in (-1, 0), which is < 1
        # So the magnitude is >= 1 * (something < 1) * 1 = something < 1
        # So the magnitude is < 1
        # So the product is in (-1, 0)
        # So for box 1 to be possible, we need A + B is odd
        if (A + B) % 2 == 1:
            possible[1] = True
        
        # Check for box 2 (third box: (0, 1))
        # The product must be in (0, 1)
        # The sign is positive
        # The magnitude must be < 1
        # For this, the sign must be positive (A + B is even)
        # And the magnitude must be < 1
        # The magnitude is the product of all toys' absolute values
        # product of A toys' absolute values is >= 1^A = 1
        # product of B toys' absolute values is in (0, 1)^B
        # product of C toys' absolute values is in (0, 1)^C
        # product of D toys' absolute values is >= 1^D = 1
        # So the product is >= 1 * (product of B toys' absolute values) * (product of C toys' absolute values) * 1
        # For this to be < 1, we need:
        # (product of B toys' absolute values) * (product of C toys' absolute values) < 1
        # Since B and C are in (-1, 0) and (0, 1), their product is in (-1, 0) * (0, 1) = (-1, 0)
        # So their product is in (-1, 0), which is < 1
        # So the magnitude is >= 1 * (something < 1) * 1 = something < 1
        # So the magnitude is < 1
        # So the product is in (0, 1)
        # So for box 2 to be possible, we need A + B is even
        if (A + B) % 2 == 0:
            possible[2] = True
        
        # Check for box 3 (fourth box: [1, inf))
        # The product must be >= 1
        # The sign is positive
        # The magnitude must be >= 1
        # For this, the sign must be positive (A + B is even)
        # And the magnitude must be >= 1
        # The magnitude is the product of all toys' absolute values
        # product of A toys' absolute values is >= 1^A = 1
        # product of B toys' absolute values is in (0, 1)^B
        # product of C toys' absolute values is in (0, 1)^C
        # product of D toys' absolute values is >= 1^D = 1
        # So the product is >= 1 * (product of B toys' absolute values) * (product of C toys' absolute values) *