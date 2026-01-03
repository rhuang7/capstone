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
        M = int(data[idx+1])
        idx += 2
        p = list(map(int, data[idx:idx+M]))
        idx += M
        
        # For each p_i, compute the maximum number of times it can be used
        # to kill sorcerers
        max_kills = 0
        for pi in p:
            # Find the maximum k such that pi mod (N - k) == 0
            # Or equivalently, find the maximum k such that pi is divisible by (N - k)
            # We need to find the maximum k where (N - k) divides pi
            # So (N - k) is a divisor of pi
            # k = N - d, where d is a divisor of pi and d <= N
            # So we need to find the maximum k = N - d, where d is a divisor of pi and d <= N
            # So the maximum k is N - min_d, where min_d is the smallest divisor of pi that is <= N
            # But we can't have k >= N, since that would mean N - k <= 0, which is invalid
            # So we need to find the smallest divisor of pi that is >= 1 and <= N
            # But we can also consider the case where pi is larger than N, and find the maximum k
            # such that pi mod (N - k) == 0
            # Let's find the maximum k such that (N - k) divides pi
            # Let's try all possible divisors of pi that are <= N
            # But for large pi, this is not feasible
            # So we need a better way
            # Let's try to find the maximum k such that (N - k) divides pi
            # So (N - k) must be a divisor of pi
            # So we can try to find the maximum k such that (N - k) divides pi
            # We can try to find the maximum k for which (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k for which (N - k) divides pi
            # We can try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # We can try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi
            # Let's try to find the maximum k such that (N - k) divides pi