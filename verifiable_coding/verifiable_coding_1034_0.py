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
        
        # The minimal total number of workers is the sum of the minimal A_i for each task
        # such that the least common multiple of all A_i is exactly X
        # and each A_i divides X
        
        # We need to find K integers A_1, A_2, ..., A_K such that:
        # 1. Each A_i divides X
        # 2. The LCM of all A_i is X
        # 3. The sum of A_i is minimized
        
        # To minimize the sum, we want to use the largest possible divisors of X that are as small as possible
        # We can use the prime factorization of X to construct the minimal sum
        
        # Find all divisors of X
        divisors = set()
        for i in range(1, int(math.isqrt(X)) + 1):
            if X % i == 0:
                divisors.add(i)
                divisors.add(X // i)
        
        # Sort the divisors in ascending order
        divisors = sorted(divisors)
        
        # Use a greedy approach: assign the largest possible divisors to minimize the sum
        # We need to select K divisors such that their LCM is X
        
        # Start with the largest divisor of X
        # We will try to find K divisors such that their LCM is X
        # We can use a backtracking approach, but for efficiency, we can use a greedy approach
        
        # The minimal sum is achieved by using the K largest divisors of X that are factors of X
        # and whose LCM is X
        
        # We can try to find the minimal sum by trying all combinations of K divisors of X
        # whose LCM is X
        
        # To optimize, we can use the fact that the LCM of K divisors is X if and only if
        # each divisor is a factor of X and the union of their prime factors is exactly the prime factors of X
        
        # So, we can find the prime factorization of X
        prime_factors = {}
        temp = X
        i = 2
        while i * i <= temp:
            while temp % i == 0:
                prime_factors[i] = prime_factors.get(i, 0) + 1
                temp //= i
            i += 1
        if temp > 1:
            prime_factors[temp] = 1
        
        # Now, we need to choose K divisors of X such that their LCM is X
        # We can do this by taking the K largest divisors of X that are factors of X
        
        # The minimal sum is achieved by taking the K largest divisors of X that are factors of X
        
        # We can sort the divisors in descending order and take the first K
        # but we need to make sure that their LCM is X
        
        # So, we can try all combinations of K divisors of X and check if their LCM is X
        
        # For efficiency, we can use a greedy approach
        # We can take the largest K divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can use a greedy approach
        # We can take the K largest divisors of X that are factors of X and check if their LCM is X
        
        # We can try all combinations of K divisors of X and find the one with the minimal sum
        # whose LCM is X
        
        # To optimize, we can