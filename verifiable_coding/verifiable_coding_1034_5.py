import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        K = int(data[index])
        X = int(data[index+1])
        index += 2
        
        # The minimal total workers is the sum of the minimal A_i for each task
        # such that the LCM of all A_i is X and each A_i divides X
        # We need to find K divisors of X that are as small as possible and have LCM X
        
        # Find all divisors of X
        divisors = set()
        for i in range(1, int(math.isqrt(X)) + 1):
            if X % i == 0:
                divisors.add(i)
                divisors.add(X // i)
        
        # Convert to a sorted list
        divisors = sorted(divisors)
        
        # We need to select K divisors of X such that their LCM is X
        # The minimal total workers is the sum of the K smallest divisors that satisfy this condition
        
        # Try to find K divisors of X such that their LCM is X
        # We need to select K divisors that include at least one of each prime factor of X
        # So we need to find K divisors of X that include all the prime factors of X
        
        # Get the prime factors of X
        prime_factors = set()
        temp = X
        i = 2
        while i * i <= temp:
            if temp % i == 0:
                prime_factors.add(i)
                while temp % i == 0:
                    temp //= i
            i += 1
        if temp > 1:
            prime_factors.add(temp)
        
        # We need to select K divisors of X that include all the prime factors of X
        # So we need to find K divisors of X such that their LCM is X
        
        # We can use a backtracking approach to find the minimal sum of K divisors of X that include all prime factors of X
        
        # To optimize, we can use a greedy approach: select the smallest K divisors of X that include all prime factors of X
        
        # Sort the divisors in increasing order
        divisors.sort()
        
        # Find the minimal sum of K divisors of X that include all prime factors of X
        # We can use a greedy approach: select the smallest K divisors of X that include all prime factors of X
        
        # We need to select K divisors of X such that their LCM is X
        # We can use a greedy approach: select the smallest K divisors of X that include all prime factors of X
        
        # We can use a greedy approach: select the smallest K divisors of X that include all prime factors of X
        
        # Start with the smallest divisor that includes all prime factors of X
        # This is X itself
        # Then select the next smallest divisors that include all prime factors of X
        
        # We can use a greedy approach: select the smallest K divisors of X that include all prime factors of X
        
        # To do this, we can use a set to track the prime factors covered so far
        # We can iterate through the divisors in increasing order and select the smallest ones that cover all prime factors
        
        # Initialize the set of covered prime factors
        covered = set()
        selected = []
        
        # Iterate through the divisors in increasing order
        for d in divisors:
            # Check if this divisor includes all prime factors of X
            # We can do this by checking if the LCM of the selected divisors and this divisor is X
            # But since we are iterating in increasing order, we can just check if the divisor includes all prime factors of X
            # This is equivalent to checking if the divisor is a multiple of all prime factors of X
            # Which is equivalent to checking if the divisor is a multiple of X
            # But that's not correct. We need to check if the divisor includes all prime factors of X
            # So we can check if the divisor is a multiple of all prime factors of X
            # Which is equivalent to checking if the divisor is a multiple of the product of all prime factors of X
            # But that's not correct either. We need to check if the divisor includes all prime factors of X
            # So we can check if the divisor is a multiple of each prime factor of X
            # Which is equivalent to checking if the divisor is a multiple of the LCM of all prime factors of X
            # Which is the product of all prime factors of X
            # Since all prime factors are distinct
            product = 1
            for p in prime_factors:
                product *= p
            if d % product == 0:
                # This divisor includes all prime factors of X
                # Add it to the selected list
                selected.append(d)
                # Update the covered prime factors
                covered.update(prime_factors)
                # If we have selected K divisors, break
                if len(selected) == K:
                    break
        
        # If we have not selected K divisors, we need to select more
        # We can select the next smallest divisors that include all prime factors of X
        # We can do this by checking each divisor in increasing order and adding it if it includes all prime factors of X
        
        # We need to select K divisors of X that include all prime factors of X
        # So we need to select K divisors of X that include all prime factors of X
        # We can do this by checking each divisor in increasing order and adding it if it includes all prime factors of X
        
        # We can use a greedy approach: select the smallest K divisors of X that include all prime factors of X
        
        # Initialize the set of covered prime factors
        covered = set()
        selected = []
        
        # Iterate through the divisors in increasing order
        for d in divisors:
            # Check if this divisor includes all prime factors of X
            # We can do this by checking if the divisor is a multiple of all prime factors of X
            # Which is equivalent to checking if the divisor is a multiple of the product of all prime factors of X
            # Since all prime factors are distinct
            product = 1
            for p in prime_factors:
                product *= p
            if d % product == 0:
                # This divisor includes all prime factors of X
                # Add it to the selected list
                selected.append(d)
                # Update the covered prime factors
                covered.update(prime_factors)
                # If we have selected K divisors, break
                if len(selected) == K:
                    break
        
        # The minimal total workers is the sum of the selected divisors
        print(sum(selected))
        
if __name__ == '__main__':
    solve()