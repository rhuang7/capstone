import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    q = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        type_counts = collections.defaultdict(list)
        type_f1 = collections.defaultdict(list)
        type_f0 = collections.defaultdict(list)
        
        for _ in range(n):
            a = int(data[idx])
            f = int(data[idx + 1])
            idx += 2
            type_counts[a].append(f)
            if f == 1:
                type_f1[a].append(f)
            else:
                type_f0[a].append(f)
        
        # For each type, sort the f=1 candies in descending order (so we can take as many as possible)
        for a in type_f1:
            type_f1[a].sort(reverse=True)
        for a in type_f0:
            type_f0[a].sort(reverse=True)
        
        # For each type, we can take at most one candy of that type in the gift
        # So we need to choose which types to include, and how many of each (but only one per type)
        # We want to maximize the number of candies, then maximize the number of f=1 candies
        
        # First, count how many f=1 candies we can take for each type
        # Then, we can take one of each type, but we want to maximize the f=1 count
        
        # Let's collect all types with at least one f=1 candy
        f1_types = []
        for a in type_f1:
            if len(type_f1[a]) > 0:
                f1_types.append(a)
        
        # Now, we can take one of each type in f1_types, but we need to decide which ones to include
        # We want to maximize the number of candies, so we can take all types (but only one per type)
        # But we also want to maximize the number of f=1 candies, so we should take as many f=1 as possible
        
        # So we can take all types (but only one per type), and for each type, take the f=1 candy if available
        # But we have to make sure that the total number of candies is maximized
        
        # Let's count how many types we can take (each type contributes 1 candy)
        max_candies = 0
        max_f1 = 0
        used_types = set()
        
        # Try to take as many types as possible, with as many f=1 as possible
        # We can take all types, but we have to choose which ones to include
        # So we can take all types, but we have to choose which ones to include (only one per type)
        # So we can take all types, but for each type, we can take one candy (either f=1 or f=0)
        # But we want to maximize the number of f=1 candies
        
        # So we can take one candy from each type, but we want to choose the one with f=1 if possible
        
        # Let's collect all types, and for each type, take the f=1 candy if available
        # If not, take the f=0 candy
        # But we can only take one candy per type
        
        # So we can take one candy per type, but we have to choose which one to take (f=1 if possible)
        # So for each type, we can take one candy (either f=1 or f=0)
        # So the maximum number of candies is the number of types
        # But we have to make sure that for each type, we take one candy (either f=1 or f=0)
        # So the maximum number of candies is the number of types, but we have to choose which ones to include
        
        # So we can take one candy per type, and for each type, we can take the f=1 candy if available
        
        # So we can take all types, but for each type, we can take one candy (either f=1 or f=0)
        # So the maximum number of candies is the number of types
        
        # So the maximum number of candies is the number of types
        # But we have to choose which types to include (all of them)
        
        # So the maximum number of candies is the number of types
        # But we have to choose which ones to include (all of them)
        
        # So the maximum number of candies is the number of types
        # And the maximum number of f=1 candies is the number of types that have at least one f=1 candy
        
        # So we can take one candy per type, and for each type, take the f=1 candy if available
        
        # So the maximum number of candies is the number of types
        # And the maximum number of f=1 candies is the number of types that have at least one f=1 candy
        
        # So the answer is (number of types, number of types with at least one f=1 candy)
        
        # But we have to make sure that we can take one candy per type
        
        # So the maximum number of candies is the number of types
        # And the maximum number of f=1 candies is the number of types with at least one f=1 candy
        
        # So the answer is (number of types, number of types with at least one f=1 candy)
        
        # But we have to make sure that for each type, we can take one candy
        
        # So the answer is (number of types, number of types with at least one f=1 candy)
        
        # So we can compute the number of types as the number of unique a_i in the input
        # And the number of types with at least one f=1 candy is the number of types in f1_types
        
        # So the answer is (number of types, len(f1_types))
        
        # So let's compute the number of types
        types = set()
        for a in type_counts:
            types.add(a)
        num_types = len(types)
        
        # The maximum number of candies is num_types
        # The maximum number of f=1 candies is len(f1_types)
        
        results.append(f"{num_types} {len(f1_types)}")
    
    print("\n".join(results))