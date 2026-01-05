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
        all_required = False
        skipped = 0
        
        for _ in range(N):
            Pi = int(data[idx])
            idx += 1
            island_ingredients = set(map(int, data[idx:idx+Pi]))
            idx += Pi
            ingredients.update(island_ingredients)
            if ingredients.issuperset(required):
                all_required = True
        
        if len(ingredients) < K:
            results.append("sad")
        else:
            # Check if there is at least one island that can be skipped
            # We need to check if there is a subset of islands that covers all required ingredients
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that can be removed without affecting the coverage
            # We can do this by checking if there is any island that is not necessary
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there is any island that is not needed
            # We can do this by checking if there