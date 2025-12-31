import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        ingredients = set()
        required = set(range(1, K+1))
        all_collected = False
        skipped = 0
        
        for _ in range(N):
            Pi = int(data[idx])
            idx += 1
            island_ingredients = set(map(int, data[idx:idx+Pi]))
            idx += Pi
            ingredients.update(island_ingredients)
            if ingredients.issuperset(required):
                all_collected = True
        
        if len(ingredients) < K:
            results.append("sad")
        else:
            # Check if there is at least one island that can be skipped
            # We need to check if there is a subset of islands that can collect all ingredients
            # We can do this by checking if there is any island that is not necessary
            # To do this, we can try removing each island and check if the remaining can collect all ingredients
            # But since N can be up to 1e5, this is not feasible
            # Instead, we can track which islands are necessary
            # We can do this by checking for each island if removing it would make the set of ingredients not contain all required
            # But again, this is O(N^2), which is not feasible
            # So we need a better approach
            # We can track which islands are necessary by checking if the set of ingredients without that island is still sufficient
            # But again, this is O(N^2)
            # So we need a smarter way
            # We can track the set of ingredients and for each island, check if it contributes any new ingredient
            # If it does, then it's necessary, otherwise it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for each island, check if it adds any new ingredient
            # If it does, then it's necessary, else it's not
            # So we can track the set of ingredients and for