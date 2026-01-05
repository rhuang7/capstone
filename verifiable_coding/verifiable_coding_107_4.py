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
        
        # Check if the special box can be first (<= -1)
        can_first = False
        # Check if the product of all toys can be <= -1
        # The product is the product of A toys <= -1, B toys in (-1, 0), C toys in (0, 1), D toys >= 1
        # We need to find if there exists a way to combine them such that the final product is <= -1
        # Since we can choose any values for the toys, we can model this with signs and possible ranges
        # For the first box to be possible, the product must be <= -1
        # Let's consider the signs
        # A toys: negative or zero (but since they are in (-infty, -1], they are negative)
        # B toys: negative (since they are in (-1, 0))
        # C toys: positive (since they are in (0, 1))
        # D toys: positive or zero (but since they are in [1, infty), they are positive)
        # So the total number of negative toys is A + B
        # The total number of positive toys is C + D
        # The product is negative if there is an odd number of negative toys
        # The product is positive if there is an even number of negative toys
        # For the product to be <= -1, it must be negative and the absolute value must be >= 1
        # So we need an odd number of negative toys
        # Let's check if it's possible to have an odd number of negative toys
        # The number of negative toys is A + B
        # We need (A + B) % 2 == 1
        # Also, the product must be <= -1
        # Let's check if it's possible to have the product <= -1
        # For that, we need at least one negative toy (since all are negative or zero)
        # But since A and B are the number of negative toys, we need at least one of them to be non-zero
        # Also, the product of all toys must be negative and have absolute value >= 1
        # Let's check if it's possible
        # For the first box to be possible:
        # 1. There must be at least one negative toy (A + B >= 1)
        # 2. The number of negative toys must be odd
        # 3. The product of all toys must be <= -1
        # Let's check these conditions
        # For the first box:
        can_first = False
        if (A + B) % 2 == 1 and (A + B) >= 1:
            # We can choose values such that the product is <= -1
            # For example, take A toys as -1, B toys as -1, C toys as 1, D toys as 1
            # The product is (-1)^A * (-1)^B * 1^C * 1^D = (-1)^(A+B)
            # Since A + B is odd, the product is -1
            # So it's possible
            can_first = True
        
        # Check if the special box can be second (in (-1, 0))
        can_second = False
        # The product must be in (-1, 0)
        # For that, the product must be negative and between -1 and 0
        # So the number of negative toys must be odd
        # Also, the product must be between -1 and 0
        # Let's check if it's possible
        # For the second box to be possible:
        # 1. There must be at least one negative toy (A + B >= 1)
        # 2. The number of negative toys must be odd
        # 3. The product of all toys must be in (-1, 0)
        # Let's check these conditions
        if (A + B) % 2 == 1 and (A + B) >= 1:
            # We can choose values such that the product is in (-1, 0)
            # For example, take A toys as -1, B toys as -1, C toys as 1, D toys as 1
            # The product is (-1)^(A+B) * 1^C * 1^D = (-1)^(A+B)
            # Since A + B is odd, the product is -1
            # But we need it to be in (-1, 0)
            # So we need to adjust the values
            # For example, take A toys as -1, B toys as -1, C toys as 1, D toys as 1
            # The product is -1
            # But we can choose values such that the product is in (-1, 0)
            # For example, take A toys as -1, B toys as -1, C toys as 0.5, D toys as 1
            # The product is (-1)^(A+B) * 0.5 * 1 = -0.5
            # Which is in (-1, 0)
            # So it's possible
            can_second = True
        
        # Check if the special box can be third ((0, 1))
        can_third = False
        # The product must be in (0, 1)
        # For that, the product must be positive and between 0 and 1
        # So the number of negative toys must be even
        # Also, the product must be between 0 and 1
        # Let's check if it's possible
        # For the third box to be possible:
        # 1. There must be at least one positive toy (C + D >= 1)
        # 2. The number of negative toys must be even
        # 3. The product of all toys must be in (0, 1)
        if (A + B) % 2 == 0 and (C + D) >= 1:
            # We can choose values such that the product is in (0, 1)
            # For example, take A toys as -1, B toys as -1, C toys as 0.5, D toys as 1
            # The product is (-1)^(A+B) * 0.5 * 1 = 0.5
            # Which is in (0, 1)
            # So it's possible
            can_third = True
        
        # Check if the special box can be fourth ([1, infty))
        can_fourth = False
        # The product must be >= 1
        # For that, the product must be positive and >= 1
        # So the number of negative toys must be even
        # Also, the product must be >= 1
        # Let's check if it's possible
        # For the fourth box to be possible:
        # 1. There must be at least one positive toy (C + D >= 1)
        # 2. The number of negative toys must be even
        # 3. The product of all toys must be >= 1
        if (A + B) % 2 == 0 and (C + D) >= 1:
            # We can choose values such that the product is >= 1
            # For example, take A toys as -1, B toys as -1, C toys as 1, D toys as 1
            # The product is (-1)^(A+B) * 1 * 1 = 1
            # Which is >= 1
            # So it's possible
            can_fourth = True
        
        results.append(f"{can_first} {can_second} {can_third} {can_fourth}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()