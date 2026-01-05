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
        
        # Precompute all possible orders of problems
        from itertools import permutations
        max_score = 0
        for order in permutations(a_p):
            # Try different training times
            # We can't try all possible training times, so we use binary search
            # But for small n (n <= 100), we can try all permutations and for each, try different training times
            # However, this is too slow. Instead, we use a binary search approach on the training time
            # We'll try to find the optimal training time for this order
            # The total time is: training_time + 10 * (number of episodes) + sum(a_i / s_i)
            # s starts at 1.0, then decreases by 10% after each episode
            # We can use binary search on the training time
            low = 0.0
            high = T
            best_training = 0.0
            best_score = 0
            for _ in range(100):
                mid = (low + high) / 2
                s = 1.0 + C * mid
                time_used = mid
                score = 0
                for i, (a, p) in enumerate(order):
                    # Watch episode
                    time_used += 10
                    if time_used > T:
                        break
                    s *= 0.9
                    # Solve problem
                    time_used += a / s
                    if time_used > T:
                        break
                    score += p
                if score > best_score:
                    best_score = score
                    best_training = mid
                # Try to increase training time if we can get more score
                # We don't know if increasing training time will help, so we try both directions
                # But for the sake of time, we'll just try to find the best possible training time
                # We can't do binary search here, so we'll try a few values
                # We'll try to find the best training time for this order
                # We'll try a few values of training time
                # This is a brute-force approach, but for small n it's manageable
                # We'll try training times in a grid
                for t in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]:
                    s = 1.0 + C * t
                    time_used = t
                    score = 0
                    for i, (a, p) in enumerate(order):
                        # Watch episode
                        time_used += 10
                        if time_used > T:
                            break
                        s *= 0.9
                        # Solve problem
                        time_used += a / s
                        if time_used > T:
                            break
                        score += p
                    if score > best_score:
                        best_score = score
                        best_training = t
            max_score = max(max_score, best_score)
        results.append(max_score)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()