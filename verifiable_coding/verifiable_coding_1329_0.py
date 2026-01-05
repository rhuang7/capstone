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
            A = list(map(int, data[idx:idx+Qi]))
            idx += Qi
            meal_sets.append((Pi, A))
        
        # Convert meal numbers to 0-based
        for i in range(M):
            for j in range(len(meal_sets[i][1])):
                meal_sets[i] = (meal_sets[i][0], [x-1 for x in meal_sets[i][1]])
        
        # Precompute set of meals
        meal_set = set(range(N))
        
        # Try all possible combinations of meal sets
        # We can use bitmask DP to represent which meals are covered
        # Since N can be up to 18, 2^18 = 262144 states is manageable
        dp = [float('inf')] * (1 << N)
        dp[0] = 0
        
        for mask in range(1 << N):
            if dp[mask] == float('inf'):
                continue
            # Try all meal sets
            for Pi, A in meal_sets:
                new_mask = mask
                for a in A:
                    new_mask |= (1 << a)
                if dp[new_mask] > dp[mask] + Pi:
                    dp[new_mask] = dp[mask] + Pi
        
        # Also consider buying individual meals
        for i in range(N):
            if dp[(1 << i)] > C[i]:
                dp[(1 << i)] = C[i]
        
        # Find the minimum cost to cover all meals
        min_cost = min(dp[(1 << N) - 1], dp[(1 << N) - 1])
        results.append(str(min_cost))
    
    print('\n'.join(results))