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
        T = float(data[idx + 1])
        idx += 2
        a_p = []
        for _ in range(n):
            a = int(data[idx])
            p = int(data[idx + 1])
            a_p.append((a, p))
            idx += 2
        
        # Try all possible orders of solving problems
        from itertools import permutations
        
        max_score = 0
        for order in permutations(range(n)):
            # Calculate the time needed for this order
            s = 1.0
            time_used = 0.0
            score = 0
            
            # Training time can be optimized
            # Try different training durations
            # We can try to find the optimal training time for this order
            # Binary search on training time
            low = 0.0
            high = T - 10 * (n + 1)  # At least 10 minutes per episode
            best_train = 0.0
            best_score = 0
            
            for train_time in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]:
                if train_time > high:
                    continue
                s = 1.0 + C * train_time
                time_used = train_time
                for i in range(n):
                    # Watch episode
                    time_used += 10.0
                    s *= 0.9
                    # Solve problem
                    time_used += a_p[order[i]][0] / s
                    score += a_p[order[i]][1]
                
                if time_used <= T:
                    if score > best_score:
                        best_score = score
                        best_train = train_time
            
            max_score = max(max_score, best_score)
        
        results.append(str(max_score))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()