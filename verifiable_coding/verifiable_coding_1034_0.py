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
        
        # The answer is the sum of the smallest K integers a_1, a_2, ..., a_K such that
        # the least common multiple (LCM) of a_1, a_2, ..., a_K is exactly X
        # and each a_i divides X.
        
        # We need to find K divisors of X such that their LCM is X and their sum is minimized.
        
        # Get all divisors of X
        divisors = set()
        for i in range(1, int(math.isqrt(X)) + 1):
            if X % i == 0:
                divisors.add(i)
                divisors.add(X // i)
        
        # Convert to list and sort
        divisors = sorted(divisors)
        
        # Try to select K divisors such that their LCM is X
        # We need to choose K divisors, and their LCM must be X
        # We can use backtracking or greedy approach.
        # Here, we use a greedy approach: choose the smallest K divisors that include X and have LCM X.
        
        # Start with the largest divisor (X) and then choose the smallest possible divisors
        # that when combined with X have LCM X.
        
        # We need to select K divisors such that their LCM is X.
        # We can use a priority queue to select the smallest possible divisors that when combined with X have LCM X.
        
        # We'll use a min-heap to select the smallest K divisors that have LCM X.
        # We'll start with X and then add the smallest possible divisors that when combined with X have LCM X.
        
        # We need to find K divisors of X such that their LCM is X.
        # We'll use a greedy approach to select the smallest K divisors that have LCM X.
        
        # We'll use a min-heap to select the smallest K divisors that have LCM X.
        # We'll start with X and then add the smallest possible divisors that when combined with X have LCM X.
        
        # Initialize the heap with X
        import heapq
        heap = [X]
        res = [X]
        
        while len(res) < K:
            # Get the smallest element from the heap
            current = heapq.heappop(heap)
            # Try to find the smallest divisor of X that is not a divisor of current
            # and when combined with current has LCM X
            for d in divisors:
                if d == current:
                    continue
                if X % d == 0 and X % current == 0:
                    if X // current == d // current:
                        continue
                    if X // d == current // d:
                        continue
                    if X % (current * d) == 0:
                        new_lcm = current * d // math.gcd(current, d)
                        if new_lcm == X:
                            heapq.heappush(heap, d)
                            res.append(d)
                            break
        
        print(sum(res))

if __name__ == '__main__':
    solve()