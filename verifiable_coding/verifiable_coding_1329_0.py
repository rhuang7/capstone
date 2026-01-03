import sys
import math
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
        sets = []
        for _ in range(M):
            Pi = int(data[idx])
            Qi = int(data[idx+1])
            idx += 2
            Ai = list(map(int, data[idx:idx+Qi]))
            idx += Qi
            sets.append((Pi, Ai))
        
        # Preprocess: for each meal, store its cost
        meal_cost = [0] * (N + 1)  # 1-based indexing
        for i in range(N):
            meal_cost[i + 1] = C[i]
        
        # Preprocess: for each meal set, store the meals it contains
        # and the cost
        set_meals = []
        for Pi, Ai in sets:
            set_meals.append((Pi, Ai))
        
        # Create a set of all meals
        all_meals = set(range(1, N + 1))
        
        # Use bitmask DP
        # dp[mask] = minimum cost to get all meals in mask
        # mask is a bitmask of N bits
        # max_mask = 1 << N
        max_mask = 1 << N
        dp = [float('inf')] * max_mask
        dp[0] = 0
        
        for mask in range(max_mask):
            if dp[mask] == float('inf'):
                continue
            # Try all meal sets
            for Pi, Ai in set_meals:
                # Check if the set contains any of the meals not yet in the mask
                # Compute the new mask
                new_mask = mask
                for meal in Ai:
                    if not (mask & (1 << (meal - 1))):
                        new_mask |= (1 << (meal - 1))
                # Update dp
                if dp[new_mask] > dp[mask] + Pi:
                    dp[new_mask] = dp[mask] + Pi
        
        # Also consider buying individual meals
        for mask in range(max_mask):
            if dp[mask] == float('inf'):
                continue
            # Add the cost of individual meals not in the mask
            cost = 0
            for i in range(N):
                if not (mask & (1 << i)):
                    cost += meal_cost[i + 1]
            if dp[mask] + cost < dp[all_meals]:
                dp[all_meals] = dp[mask] + cost
        
        results.append(str(dp[all_meals]))
    
    print('\n'.join(results))