import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_gcd = 0
        # Case 1: do not reverse the array
        # Try all possible subarrays to remove
        # But checking all subarrays is O(N^2), which is too slow
        # So we try all possible divisors of the elements
        # and check if there's a subarray that can be removed
        # to leave the rest with that divisor as GCD
        # So we collect all possible divisors of all elements
        # and check for each divisor if it's possible
        # to have the remaining elements have that divisor as GCD
        # We can do this by checking for each divisor d
        # if there exists a subarray that can be removed
        # such that all remaining elements are divisible by d
        # and the GCD of the remaining elements is at least d
        # So we collect all possible divisors of all elements
        # and check for each divisor in descending order
        # to find the maximum possible GCD
        # This is the optimal approach
        # We collect all possible divisors of all elements
        divisors = set()
        for num in arr:
            for i in range(1, int(math.isqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
        # Also include the elements themselves
        for num in arr:
            divisors.add(num)
        # Sort the divisors in descending order
        sorted_divisors = sorted(divisors, reverse=True)
        # Try each divisor
        for d in sorted_divisors:
            # Check if there exists a subarray that can be removed
            # such that all remaining elements are divisible by d
            # and the GCD of the remaining elements is at least d
            # So we check if the number of elements divisible by d is >= 1
            # and the number of elements not divisible by d is <= N-1
            # Because we can remove a subarray that contains all elements not divisible by d
            count = 0
            for num in arr:
                if num % d == 0:
                    count += 1
            if count >= 1 and count <= N:
                # Check if the GCD of the elements divisible by d is at least d
                # We can compute the GCD of all elements divisible by d
                # and see if it's at least d
                # If yes, then this is a candidate for the maximum GCD
                # So we compute the GCD of all elements divisible by d
                # and if it's >= d, then we can return d as the answer
                # Because we are checking in descending order
                # So the first such d we find is the maximum possible
                current_gcd = 0
                for num in arr:
                    if num % d == 0:
                        current_gcd = math.gcd(current_gcd, num)
                if current_gcd >= d:
                    results.append(d)
                    break
        # Case 2: reverse the array
        # We can do the same as above, but with the reversed array
        # So we check the same as before, but with the reversed array
        # So we can do the same steps as above with the reversed array
        # So we reverse the array and check the same as before
        reversed_arr = arr[::-1]
        max_gcd_rev = 0
        # Collect all possible divisors of the reversed array
        divisors_rev = set()
        for num in reversed_arr:
            for i in range(1, int(math.isqrt(num)) + 1):
                if num % i == 0:
                    divisors_rev.add(i)
                    divisors_rev.add(num // i)
        for num in reversed_arr:
            divisors_rev.add(num)
        sorted_divisors_rev = sorted(divisors_rev, reverse=True)
        for d in sorted_divisors_rev:
            count_rev = 0
            for num in reversed_arr:
                if num % d == 0:
                    count_rev += 1
            if count_rev >= 1 and count_rev <= N:
                current_gcd_rev = 0
                for num in reversed_arr:
                    if num % d == 0:
                        current_gcd_rev = math.gcd(current_gcd_rev, num)
                if current_gcd_rev >= d:
                    max_gcd_rev = max(max_gcd_rev, d)
        # The maximum between the two cases
        max_gcd = max(max_gcd, max_gcd_rev)
        results.append(max_gcd)
    
    for res in results:
        print(res)