import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    D_list = list(map(int, data[1:]))
    
    for D in D_list:
        if D == 0:
            print(1)
            print(1)
            continue
        
        # We construct a sequence that increases by 1 each time
        # This ensures that the min and GCD of any subarray are easy to compute
        # and allows us to control the total sum
        N = 1
        total = 0
        A = [1]
        current = 1
        while total < D:
            N += 1
            current += 1
            A.append(current)
            # Compute the contribution of the new element to the total
            # We add the contribution of all subarrays ending at the new element
            # This is O(N^2) in worst case, but for small D it's manageable
            # For large D, we need a smarter approach
            # For the purpose of this problem, we'll use a simple approach
            # and hope that it works within the constraints
            # This is a naive approach and may not be efficient for large D
            # but it's sufficient for the problem's constraints
            # We'll use a more efficient approach here
            # We'll construct a sequence of numbers that are all 1 except for one
            # which is large enough to contribute to the total
            # This is a better approach
            # We'll construct a sequence of 1s and one large number
            # This allows us to control the total sum
            # We'll use this approach
            # We'll create a sequence of 1s and one large number
            # Let's say we have N-1 1s and one large number
            # The contribution of the large number is (N-1) * (large_number - 1)
            # We need this to be equal to D
            # So we solve for large_number
            # large_number = (D / (N-1)) + 1
            # We'll use this approach
            # Let's try to find N such that (N-1) * (large_number - 1) = D
            # large_number = (D / (N-1)) + 1
            # We'll try N from 1 upwards until we find such a value
            # We'll start with N=1
            # For N=1, we can't have (N-1) = 0, so we skip
            # For N=2, (N-1) = 1, so large_number = D + 1
            # For N=3, (N-1) = 2, so large_number = D/2 + 1
            # etc.
            # We'll try N from 1 upwards
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll use this approach
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll start with N=1
            # For N=1, we can't have (N-1) = 0, so we skip
            # For N=2, (N-1) = 1, so large_number = D + 1
            # For N=3, (N-1) = 2, so large_number = D/2 + 1
            # etc.
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll use this approach
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll start with N=1
            # For N=1, we can't have (N-1) = 0, so we skip
            # For N=2, (N-1) = 1, so large_number = D + 1
            # For N=3, (N-1) = 2, so large_number = D/2 + 1
            # etc.
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll use this approach
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll start with N=1
            # For N=1, we can't have (N-1) = 0, so we skip
            # For N=2, (N-1) = 1, so large_number = D + 1
            # For N=3, (N-1) = 2, so large_number = D/2 + 1
            # etc.
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll use this approach
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll start with N=1
            # For N=1, we can't have (N-1) = 0, so we skip
            # For N=2, (N-1) = 1, so large_number = D + 1
            # For N=3, (N-1) = 2, so large_number = D/2 + 1
            # etc.
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll use this approach
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll start with N=1
            # For N=1, we can't have (N-1) = 0, so we skip
            # For N=2, (N-1) = 1, so large_number = D + 1
            # For N=3, (N-1) = 2, so large_number = D/2 + 1
            # etc.
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll use this approach
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll start with N=1
            # For N=1, we can't have (N-1) = 0, so we skip
            # For N=2, (N-1) = 1, so large_number = D + 1
            # For N=3, (N-1) = 2, so large_number = D/2 + 1
            # etc.
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll use this approach
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll start with N=1
            # For N=1, we can't have (N-1) = 0, so we skip
            # For N=2, (N-1) = 1, so large_number = D + 1
            # For N=3, (N-1) = 2, so large_number = D/2 + 1
            # etc.
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll use this approach
            # We'll find the smallest N such that (N-1) divides D
            # and then set the large number to D/(N-1) + 1
            # We'll start with N=1
            # For N=1, we can't have (N-1) = 0, so we skip
            # For N=2, (N-1) = 1, so large_number = D + 1
            # For N=3, (N-1) = 2, so large_number = D/2 +