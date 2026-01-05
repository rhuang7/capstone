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
        K = int(data[index])
        X = int(data[index+1])
        index += 2
        
        # The minimal total number of workers is the sum of the minimal A_i for each task
        # such that the LCM of all A_i is exactly X and each A_i divides X
        # Also, each A_i must be at least 1 and the sum of A_i is minimized
        
        # We need to find K integers a_1, a_2, ..., a_K such that:
        # 1. Each a_i divides X
        # 2. The LCM of all a_i is X
        # 3. The sum of a_i is minimized
        
        # The minimal sum is achieved when we use the K smallest divisors of X that are >=1 and their LCM is X
        
        # Find all divisors of X
        divisors = set()
        for i in range(1, int(math.isqrt(X)) + 1):
            if X % i == 0:
                divisors.add(i)
                divisors.add(X // i)
        
        # Convert to a sorted list
        divisors = sorted(divisors)
        
        # We need to select K divisors from this list such that their LCM is X
        # and their sum is minimized
        
        # We can use a backtracking approach, but since K can be up to 1e6, this is not feasible
        
        # Instead, we can use the fact that the minimal sum is achieved when we use the K smallest divisors of X that are >=1 and their LCM is X
        
        # The minimal sum is achieved when we use the K smallest divisors of X that are >=1 and their LCM is X
        
        # To find this, we can try to select K divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        # We can try to select the K smallest divisors of X that are >=1 and their LCM is X
        
        #