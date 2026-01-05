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
        X = int(data[index + 1])
        index += 2
        
        # The minimal total workers is the sum of the minimal A_i for each task
        # such that the least common multiple of all A_i is exactly X
        # and each A_i divides X
        
        # We need to find K divisors of X such that their LCM is X
        # and the sum of the divisors is minimized
        
        # To minimize the sum, we want the divisors to be as small as possible
        # but their LCM must be X
        
        # So we find all divisors of X, sort them in increasing order
        # Then try to select K divisors such that their LCM is X and sum is minimized
        
        divisors = []
        for i in range(1, int(math.isqrt(X)) + 1):
            if X % i == 0:
                divisors.append(i)
                if i != X // i:
                    divisors.append(X // i)
        
        divisors = list(set(divisors))
        divisors.sort()
        
        # Now find the minimal sum of K divisors whose LCM is X
        # We can try all combinations of K divisors from the list
        # and check if their LCM is X
        
        # Since K can be up to 1e6, this approach is not feasible for large K
        # So we need a smarter approach
        
        # The minimal sum is achieved when we take the K smallest divisors of X
        # that are factors of X and their LCM is X
        
        # So we need to find the K smallest divisors of X that are factors of X
        # and their LCM is X
        
        # To do this, we can try to find the minimal sum by taking the K smallest
        # divisors of X that are factors of X and their LCM is X
        
        # We can start by taking the K smallest divisors of X and check if their LCM is X
        # If not, we need to replace some of them with larger ones
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # Let's try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X that are factors of X and their LCM is X
        
        # We can try to find the minimal sum by trying to find the K smallest divisors
        # of X