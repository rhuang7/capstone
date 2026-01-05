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
                type_f1[a].append(1)
            else:
                type_f0[a].append(0)
        
        # For each type, count how many f=1 and f=0 candies
        type_f1_counts = {}
        type_f0_counts = {}
        for a in type_counts:
            type_f1_counts[a] = len(type_f1[a])
            type_f0_counts[a] = len(type_f0[a])
        
        # We want to maximize the number of candies, and among those, maximize f=1
        # So we try to take as many as possible, but with distinct counts per type
        
        # We'll use a greedy approach: sort types by the number of f=1 candies in descending order
        types = list(type_f1_counts.keys())
        types.sort(key=lambda x: -type_f1_counts[x])
        
        # We'll track how many candies we can take and how many f=1
        max_total = 0
        max_f1 = 0
        used_counts = set()
        
        for a in types:
            # Try to take as many as possible of this type, but with a count not already used
            # We can take up to min(type_f1_counts[a], type_f0_counts[a]) candies
            # But we need to choose a count that is not already used
            # So we try to take the maximum possible count for this type
            # We try from the maximum possible down to 0
            # We want to take as many as possible, but with distinct counts
            # We also want to maximize f=1, so we prefer taking more f=1 candies
            # So we take as many as possible of this type, but with a count not used yet
            # We try to take the maximum possible count for this type, but not already used
            # We can take up to min(type_f1_counts[a], type_f0_counts[a]) candies
            # But we need to choose a count that is not already used
            # So we try to take the maximum possible count for this type, but not already used
            # We try from the maximum possible down to 0
            max_possible = min(type_f1_counts[a], type_f0_counts[a])
            for cnt in range(max_possible, -1, -1):
                if cnt not in used_counts:
                    used_counts.add(cnt)
                    total = cnt
                    f1 = type_f1_counts[a]
                    max_total += total
                    max_f1 += f1
                    break
        
        results.append(f"{max_total} {max_f1}")
    
    print("\n".join(results))