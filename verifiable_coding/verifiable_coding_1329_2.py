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
        
        # Create a set of all meals
        all_meals = set(range(1, N+1))
        
        # Precompute the cost of buying each meal individually
        cost_individual = {i: C[i-1] for i in range(1, N+1)}
        
        # Precompute the cost of each meal set
        cost_set = []
        for Pi, A in meal_sets:
            # Check if the meal set contains all meals
            if set(A) == all_meals:
                cost_set.append(Pi)
            else:
                cost_set.append(float('inf'))
        
        # If there is a meal set that contains all meals, compare with the individual cost
        if any(cost < float('inf') for cost in cost_set):
            min_total = min(cost_set)
        else:
            # Try combinations of meal sets that cover all meals
            # This is a knapsack-like problem, but with sets
            # We need to find a collection of meal sets that together cover all meals
            # and minimize the total cost
            
            # We can use a bitmask approach for small N (up to 18)
            # Since N can be up to 18, we can use a bitmask of size 18
            # Each bit represents whether a meal is covered
            # We can use dynamic programming to find the minimum cost to cover each bitmask
            
            # Initialize dp array where dp[mask] is the minimum cost to cover the meals in mask
            dp = [float('inf')] * (1 << N)
            dp[0] = 0
            
            for mask in range(1 << N):
                if dp[mask] == float('inf'):
                    continue
                # Try each meal set
                for Pi, A in meal_sets:
                    # Compute the mask of meals covered by this set
                    set_mask = 0
                    for meal in A:
                        set_mask |= (1 << (meal - 1))
                    # Compute the new mask after adding this set
                    new_mask = mask | set_mask
                    # Update dp if this set is useful
                    if dp[new_mask] > dp[mask] + Pi:
                        dp[new_mask] = dp[mask] + Pi
            
            # The answer is the minimum cost to cover all meals
            min_total = dp[(1 << N) - 1]
        
        results.append(str(min_total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()