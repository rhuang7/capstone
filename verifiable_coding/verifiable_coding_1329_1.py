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
        
        meal_set = []
        for _ in range(M):
            Pi = int(data[idx])
            Qi = int(data[idx+1])
            idx += 2
            Ai = list(map(int, data[idx:idx+Qi]))
            idx += Qi
            meal_set.append((Pi, Ai))
        
        # Create a set of all meals
        all_meals = set(range(1, N+1))
        
        # Preprocess meal sets to include only those that contain all meals
        valid_sets = []
        for Pi, Ai in meal_set:
            if set(Ai) == all_meals:
                valid_sets.append(Pi)
        
        # If there is a set that contains all meals, consider it
        if valid_sets:
            results.append(min(valid_sets))
            continue
        
        # Otherwise, use dynamic programming to find the minimal cost
        # We need to have at least one of each meal
        # We'll use a bitmask DP approach
        # Since N can be up to 18, 2^18 is manageable (262144)
        dp = [float('inf')] * (1 << N)
        dp[0] = 0
        
        for i in range(1 << N):
            if dp[i] == float('inf'):
                continue
            # Try each meal set
            for Pi, Ai in meal_set:
                # Check if the set contains any of the meals not yet covered
                mask = 0
                for meal in Ai:
                    mask |= (1 << (meal - 1))
                # Update dp[i | mask]
                if dp[i | mask] > dp[i] + Pi:
                    dp[i | mask] = dp[i] + Pi
        
        # Find the minimal cost to have all meals
        min_cost = min(dp[(1 << N) - 1], sum(C))
        results.append(min_cost)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()