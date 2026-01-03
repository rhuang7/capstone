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
        type_count = collections.defaultdict(list)
        f_count = collections.defaultdict(list)
        for _ in range(n):
            a = int(data[idx])
            f = int(data[idx + 1])
            idx += 2
            type_count[a].append(f)
            f_count[a].append(f)
        
        # For each type, count how many f=1 and f=0 candies
        type_f1 = {}
        type_f0 = {}
        for a in type_count:
            type_f1[a] = sum(1 for f in type_count[a] if f == 1)
            type_f0[a] = sum(1 for f in type_count[a] if f == 0)
        
        # We need to select for each type a number of candies (k) such that all k's are distinct
        # We want to maximize the total number of candies, and among those, maximize the number of f=1 candies
        
        # We'll try to assign as many as possible, starting from the types with more f=1 candies
        # We'll use a priority queue to select the types with the most f=1 candies first
        
        # Create a list of (f1, f0, type) for each type
        types = []
        for a in type_count:
            types.append((type_f1[a], type_f0[a], a))
        
        # Sort types by f1 in descending order
        types.sort(reverse=True)
        
        # We'll use a greedy approach to assign the maximum possible number of candies
        # We'll use a set to track the counts we've already used
        used_counts = set()
        total_candies = 0
        total_f1 = 0
        
        for f1, f0, a in types:
            # Try to assign as many as possible without repeating counts
            # We'll try to assign the maximum possible count for this type
            # The maximum possible count for this type is min(f1 + f0, max_count)
            # We'll try to assign the largest possible count that hasn't been used yet
            max_possible = min(f1 + f0, len(used_counts) + 1)
            for k in range(max_possible, 0, -1):
                if k not in used_counts:
                    used_counts.add(k)
                    total_candies += k
                    total_f1 += k * (f1 / (f1 + f0))  # This is a simplification, we'll compute it properly later
                    break
        
        # Now, we need to compute the exact number of f1 candies
        # We'll recompute the total_f1 properly
        total_f1 = 0
        used_counts = set()
        for f1, f0, a in types:
            # Try to assign as many as possible without repeating counts
            # We'll try to assign the largest possible count that hasn't been used yet
            max_possible = min(f1 + f0, len(used_counts) + 1)
            for k in range(max_possible, 0, -1):
                if k not in used_counts:
                    used_counts.add(k)
                    total_candies += k
                    total_f1 += min(k, f1)
                    break
        
        results.append(f"{total_candies} {total_f1}")
    
    print("\n".join(results))