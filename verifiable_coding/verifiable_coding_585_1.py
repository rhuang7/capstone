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
            # Find the maximum k such that k * pi <= N * (k + 1) - 1
            # This is equivalent to finding the maximum k such that k * (pi - 1) <= N * k
            # Which simplifies to pi <= N + 1
            # But we need to find the maximum k such that k * pi <= N * (k + 1) - 1
            # Rearranged: k * (pi - N) <= N - 1
            # So k <= (N - 1) / (N - pi)
            # But we need to handle the case when pi > N
            if pi > N:
                continue
            # Compute the maximum k for this pi
            # The maximum k is floor((N - 1) / (N - pi))
            denominator = N - pi
            if denominator == 0:
                continue
            k = (N - 1) // denominator
            max_kills += k
        
        results.append(str(max_kills))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()