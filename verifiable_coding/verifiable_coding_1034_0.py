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
        # such that the least common multiple of all A_i is X
        # We need to find K numbers A_1, A_2, ..., A_K such that LCM(A_1, A_2, ..., A_K) = X
        # and sum(A_i) is minimized
        
        # To minimize the sum, we want to use as many as possible of the largest divisors of X
        # that are as small as possible
        # We can find all the divisors of X, sort them in increasing order, and then select the K largest ones
        
        # Find all divisors of X
        divisors = set()
        for i in range(1, int(math.isqrt(X)) + 1):
            if X % i == 0:
                divisors.add(i)
                divisors.add(X // i)
        
        # Sort the divisors in increasing order
        divisors = sorted(divisors)
        
        # Take the K largest divisors
        selected = divisors[-K:]
        
        # Sum them
        print(sum(selected))
        
if __name__ == '__main__':
    solve()