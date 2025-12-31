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
        
        # Create a set of all meals
        all_meals = set(range(1, N+1))
        
        # Precompute the cost of buying all meals separately
        separate_cost = sum(C)
        
        # Try all possible combinations of meal sets
        # Use bitmask to represent which sets are chosen
        min_cost = separate_cost
        for mask in range(1 << M):
            selected_sets = []
            total_meals = set()
            total_cost = 0
            for i in range(M):
                if (mask >> i) & 1:
                    selected_sets.append(meal_sets[i])
                    total_cost += meal_sets[i][0]
                    for meal in meal_sets[i][1]:
                        total_meals.add(meal)
            # Check if all meals are covered
            if len(total_meals) == N:
                if total_cost < min_cost:
                    min_cost = total_cost
        
        results.append(str(min_cost))
    
    print('\n'.join(results))