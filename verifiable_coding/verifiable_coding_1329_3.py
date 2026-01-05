import sys
import itertools

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
        
        # Convert meal numbers to 0-based index
        meal_set_indices = [a-1 for a in Ai]
        
        # Precompute the cost of each meal
        meal_cost = C
        
        # For each meal set, compute the cost of buying it
        set_cost = []
        for Pi, Ai in meal_sets:
            # Check if the set contains all meals
            if len(set(Ai)) != len(Ai):
                continue
            # Check if the set contains all required meals
            required_meals = set(range(N))
            set_meals = set(Ai)
            if not required_meals.issubset(set_meals):
                continue
            # Compute the cost of the set
            set_cost.append(Pi)
        
        # If no set contains all meals, buy all separately
        if not set_cost:
            total = sum(C)
            results.append(str(total))
            continue
        
        # Try all combinations of sets and individual meals
        # We need to find a combination that includes all meals
        # We can use bitmask DP
        # Let dp[mask] be the minimum cost to get the meals in mask
        dp = [float('inf')] * (1 << N)
        dp[0] = 0
        
        for mask in range(1 << N):
            if dp[mask] == float('inf'):
                continue
            # Try adding a set that includes some of the meals not yet in the mask
            for Pi, Ai in meal_sets:
                set_meals = set(Ai)
                new_mask = mask | set_meals
                if new_mask != mask:
                    if dp[new_mask] > dp[mask] + Pi:
                        dp[new_mask] = dp[mask] + Pi
            # Try adding individual meals
            for i in range(N):
                if not (mask & (1 << i)):
                    if dp[mask | (1 << i)] > dp[mask] + C[i]:
                        dp[mask | (1 << i)] = dp[mask] + C[i]
        
        # The answer is the minimum cost to get all meals
        results.append(str(dp[(1 << N) - 1]))
    
    print('\n'.join(results))