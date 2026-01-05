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
        X = int(data[index + 1])
        index += 2
        
        # The minimal total number of workers is the sum of the minimal A_i for each task i
        # such that the least common multiple of all A_i is exactly X
        # and each A_i divides X
        
        # We need to find K divisors of X such that their LCM is X
        # and the sum of these divisors is minimized
        
        # Generate all divisors of X
        divisors = []
        for i in range(1, int(math.isqrt(X)) + 1):
            if X % i == 0:
                divisors.append(i)
                if i != X // i:
                    divisors.append(X // i)
        
        # Sort divisors in ascending order
        divisors.sort()
        
        # Use a backtracking approach to find K divisors whose LCM is X
        # and sum is minimized
        
        def backtrack(pos, current_lcm, current_sum, count):
            if count == K:
                if current_lcm == X:
                    return current_sum
                else:
                    return float('inf')
            
            if pos >= len(divisors):
                return float('inf')
            
            # Try to take the current divisor
            res = backtrack(pos + 1, lcm(current_lcm, divisors[pos]), current_sum + divisors[pos], count + 1)
            
            # Try to skip the current divisor
            res = min(res, backtrack(pos + 1, current_lcm, current_sum, count))
            
            return res
        
        def lcm(a, b):
            return a * b // math.gcd(a, b)
        
        result = backtrack(0, 1, 0, 0)
        print(result)

if __name__ == '__main__':
    solve()