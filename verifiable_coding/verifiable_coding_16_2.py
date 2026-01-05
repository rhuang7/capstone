import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    tc = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(tc):
        n = int(data[idx])
        idx += 1
        C = float(data[idx])
        T = float(data[idx+1])
        idx += 2
        a_p = []
        for _ in range(n):
            a = int(data[idx])
            p = int(data[idx+1])
            a_p.append((a, p))
            idx += 2
        
        # Precompute all possible orders of solving problems
        from itertools import permutations
        max_score = 0
        for order in permutations(range(n)):
            # Calculate total time needed for this order
            s = 1.0
            time_used = 0.0
            score = 0
            for i in range(n):
                # Watch an episode
                time_used += 10.0
                s *= 0.9
                # Solve the problem
                time_needed = a_p[order[i]][0] / s
                time_used += time_needed
                if time_used > T:
                    break
                score += a_p[order[i]][1]
            if time_used <= T:
                max_score = max(max_score, score)
        
        results.append(max_score)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()