import sys
import itertools
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, M = int(data[idx]), int(data[idx+1])
        idx += 2
        C = list(map(int, data[idx:idx+N]))
        idx += N
        meal_sets = []
        for _ in range(M):
            Pi = int(data[idx])
            Qi = int(data[idx+1])
            idx += 2
            Ai = list(map(int, data[idx:idx+Qi]))
            idx += Qi
            meal_sets.append((Pi, Ai))
        
        # Convert meal numbers to 0-based
        meal_set_indices = [a-1 for a in Ai]
        # Create a list of meal sets with their indices
        sets = []
        for Pi, Ai in meal_sets:
            indices = [a-1 for a in Ai]
            sets.append((Pi, indices))
        
        # Precompute the cost of each meal
        meal_cost = C
        
        # For each meal, find the best meal set that includes it
        best_set_for_meal = [None] * N
        for Pi, indices in sets:
            for i in indices:
                if best_set_for_meal[i] is None or Pi < meal_cost[i]:
                    best_set_for_meal[i] = Pi
        
        # Check if all meals can be covered by a single set
        all_covered = True
        for i in range(N):
            if best_set_for_meal[i] is None:
                all_covered = False
                break
        if all_covered:
            results.append(min(best_set_for_meal))
            continue
        
        # Try all combinations of meal sets
        # We need to find a subset of sets that covers all meals
        # We can use bitmask DP for small N (up to 18)
        # Precompute which sets cover which meals
        set_meals = []
        for Pi, indices in sets:
            set_meals.append(indices)
        
        # Precompute the set of meals covered by each set
        set_mask = []
        for indices in set_meals:
            mask = 0
            for i in indices:
                mask |= (1 << i)
            set_mask.append(mask)
        
        # Use bitmask DP to find the minimum cost to cover all meals
        # dp[mask] = minimum cost to cover the meals in mask
        dp = [float('inf')] * (1 << N)
        dp[0] = 0
        for mask in range(1 << N):
            if dp[mask] == float('inf'):
                continue
            for i in range(M):
                new_mask = mask | set_mask[i]
                cost = dp[mask] + sets[i][0]
                if cost < dp[new_mask]:
                    dp[new_mask] = cost
        results.append(dp[(1 << N) - 1])
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()