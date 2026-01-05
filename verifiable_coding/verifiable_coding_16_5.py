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
        # We'll use a brute-force approach with some optimizations
        # Since n is small (<= 100), but trying all permutations is too slow
        # Instead, we'll try all possible subsets of problems to solve, in all possible orders
        
        max_score = 0
        # Try all possible subsets of problems to solve (up to 100)
        # For each subset, try all possible orders
        # We'll use a greedy approach for the order: sort by a_i / s_i (with s_i being the current skill)
        # But since s_i changes with each episode, we need to simulate
        
        # Precompute all possible orders of problems
        # Since n is small, we can generate all permutations
        from itertools import permutations
        
        for perm in permutations(a_p):
            # Try to solve this permutation of problems
            # We'll simulate the process
            # Initial skill is 1.0
            s = 1.0
            time_used = 0.0
            score = 0
            # We can choose to train before solving any problem
            # So we need to decide how much to train
            # We'll try all possible training times (with some precision)
            # But since it's continuous, we'll use binary search
            # But for simplicity, we'll try all possible training times with some precision
            # We'll try all possible training times in a grid of 0.0 to T
            # But this is not feasible for large T
            # So instead, we'll try to find the optimal training time using binary search
            
            # Binary search for the optimal training time
            low = 0.0
            high = T
            best_train_time = 0.0
            best_score = 0
            for _ in range(100):
                mid = (low + high) / 2
                # Try training for mid minutes
                s = 1.0 + C * mid
                time_used = mid
                # Now solve the problems in the order perm
                for a, p in perm:
                    # Watch one episode
                    time_used += 10.0
                    if time_used > T:
                        break
                    s *= 0.9
                    # Solve the problem
                    time_needed = a / s
                    time_used += time_needed
                    if time_used > T:
                        break
                    score += p
                if score > best_score:
                    best_score = score
                    best_train_time = mid
            max_score = max(max_score, best_score)
        
        results.append(max_score)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()