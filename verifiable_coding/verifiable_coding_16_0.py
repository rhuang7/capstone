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
            # Try different training times
            # We'll use binary search on the training time
            # Since training is before solving any problem, we can try different training times
            # and see what's the best score
            # We'll try training times in a range from 0 to T - 10*n (since each problem needs 10 mins to watch)
            # We'll use binary search on the training time
            # But since the problem is complex, we'll try a grid search over possible training times
            # with a step of 0.001 to cover all possibilities
            # But to optimize, we'll try a binary search approach
            # However, given the small n (up to 100), we can try all possible orders and for each order, try different training times
            # So we'll try all possible orders and for each order, try different training times
            # But since the problem is complex, we'll use a binary search approach for training time
            
            # Binary search on training time
            low = 0.0
            high = T - 10 * n
            best_score = 0
            for _ in range(100):
                mid = (low + high) / 2
                s = 1.0 + C * mid
                time_used = mid
                for i in range(n):
                    # Watch one episode
                    time_used += 10.0
                    s *= 0.9
                    # Solve the problem
                    time_used += a_p[order[i]][0] / s
                    if time_used > T:
                        break
                if time_used <= T:
                    best_score = max(best_score, a_p[order[0]][1])
                    # Try to increase training time
                    low = mid
                else:
                    # Try to decrease training time
                    high = mid
            max_score = max(max_score, best_score)
        
        results.append(max_score)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()