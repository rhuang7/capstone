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
        # such that the least common multiple (LCM) of all A_i is X
        # And each A_i must divide X
        # We need to find K divisors of X that are as small as possible and have LCM X
        
        # Find all divisors of X
        divisors = set()
        for i in range(1, int(math.isqrt(X)) + 1):
            if X % i == 0:
                divisors.add(i)
                divisors.add(X // i)
        
        # Sort the divisors in ascending order
        divisors = sorted(divisors)
        
        # Try to find K divisors such that their LCM is X
        # We need to choose K divisors from the list of divisors of X
        # and find the combination with the smallest sum
        # We will use a backtracking approach to find the minimal sum
        
        def backtrack(start, count, current_lcm, current_sum):
            if count == K:
                if current_lcm == X:
                    return current_sum
                return float('inf')
            
            min_sum = float('inf')
            for i in range(start, len(divisors)):
                d = divisors[i]
                new_lcm = current_lcm
                if current_lcm != 0:
                    new_lcm = current_lcm * d // math.gcd(current_lcm, d)
                if new_lcm > X:
                    continue
                res = backtrack(i, count + 1, new_lcm, current_sum + d)
                if res < min_sum:
                    min_sum = res
            return min_sum
        
        result = backtrack(0, 0, 0, 0)
        print(result)

if __name__ == '__main__':
    solve()