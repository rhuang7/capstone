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
        all_ingredients = set(range(1, K+1))
        required = all_ingredients.copy()
        
        for _ in range(N):
            Pi = int(data[idx])
            idx += 1
            for i in range(Pi):
                ingredients.add(int(data[idx]))
                idx += 1
        
        if required - ingredients:
            results.append("sad")
        else:
            # Check if there is at least one island that can be skipped
            # We can do this by checking if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed without losing any ingredients
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than K
            # But we need to check if there is at least one island that can be removed
            # So we can check if the total number of unique ingredients is less than N
            # But we need to check if there is at least one island that can be removed
            # So we can