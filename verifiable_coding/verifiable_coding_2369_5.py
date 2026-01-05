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
        type_f = []
        for _ in range(n):
            a = int(data[idx])
            f = int(data[idx+1])
            type_f.append((a, f))
            idx += 2
        
        # Group by type
        type_dict = collections.defaultdict(list)
        for a, f in type_f:
            type_dict[a].append(f)
        
        # For each type, count the number of f=1 and f=0
        type_counts = []
        for a in type_dict:
            f1 = sum(1 for f in type_dict[a] if f == 1)
            f0 = len(type_dict[a]) - f1
            type_counts.append((f1, f0))
        
        # Sort types by f1 (we want to maximize f1 first)
        type_counts.sort(reverse=True, key=lambda x: x[0])
        
        # Now, try to assign counts to each type
        # We need to choose a count for each type such that all counts are distinct
        # And we want to maximize the total count, and then maximize f1
        
        # We'll use a greedy approach: try to assign the maximum possible count for each type
        # but ensuring that counts are unique
        
        # We'll use a set to track used counts
        used = set()
        total = 0
        total_f1 = 0
        
        for f1, f0 in type_counts:
            # Try to assign the maximum possible count for this type
            # starting from the maximum possible (f1 + f0)
            # but ensuring it's not already used
            # and also ensuring that it's at most the total available (f1 + f0)
            # and also ensuring that it's not more than the maximum possible (which is the number of types)
            # since all counts must be distinct
            max_possible = min(f1 + f0, len(used) + 1)
            for cnt in range(min(f1 + f0, len(used) + 1), 0, -1):
                if cnt not in used:
                    used.add(cnt)
                    total += cnt
                    total_f1 += cnt * (f1 / (f1 + f0))  # approximate, but we'll adjust later
                    break
        
        # Now, we need to adjust to maximize f1
        # We'll try to find a way to increase f1 by swapping counts
        # We'll keep track of how many f1 and f0 we have for each type
        # and try to find a way to increase the total f1
        
        # We'll create a list of (f1, f0, count) for each type
        # where count is the number of candies we've chosen for that type
        # and we'll try to maximize f1
        
        # Rebuild the list of (f1, f0, count) for each type
        # and sort by count in descending order
        type_list = []
        for a in type_dict:
            f1 = sum(1 for f in type_dict[a] if f == 1)
            f0 = len(type_dict[a]) - f1
            # count is the number of candies we've chosen for this type
            # we'll compute it later
            type_list.append((f1, f0))
        
        # Sort by f1 in descending order
        type_list.sort(reverse=True, key=lambda x: x[0])
        
        # Now, try to assign counts again, but this time, we'll prioritize f1
        used = set()
        total = 0
        total_f1 = 0
        for f1, f0 in type_list:
            # Try to assign the maximum possible count for this type
            # but ensuring it's not already used
            # and also ensuring that it's at most the total available (f1 + f0)
            # and also ensuring that it's not more than the maximum possible (which is the number of types)
            max_possible = min(f1 + f0, len(used) + 1)
            for cnt in range(min(f1 + f0, len(used) + 1), 0, -1):
                if cnt not in used:
                    used.add(cnt)
                    total += cnt
                    total_f1 += cnt * (f1 / (f1 + f0))  # approximate, but we'll adjust later
                    break
        
        # Now, we need to adjust to maximize f1
        # We'll try to find a way to increase f1 by swapping counts
        # We'll keep track of how many f1 and f0 we have for each type
        # and try to find a way to increase the total f1
        
        # We'll create a list of (f1, f0, count) for each type
        # where count is the number of candies we've chosen for that type
        # and we'll try to maximize f1
        
        # Rebuild the list of (f1, f0, count) for each type
        # and sort by count in descending order
        type_list = []
        for a in type_dict:
            f1 = sum(1 for f in type_dict[a] if f == 1)
            f0 = len(type_dict[a]) - f1
            # count is the number of candies we've chosen for this type
            # we'll compute it later
            type_list.append((f1, f0))
        
        # Sort by f1 in descending order
        type_list.sort(reverse=True, key=lambda x: x[0])
        
        # Now, try to assign counts again, but this time, we'll prioritize f1
        used = set()
        total = 0
        total_f1 = 0
        for f1, f0 in type_list:
            # Try to assign the maximum possible count for this type
            # but ensuring it's not already used
            # and also ensuring that it's at most the total available (f1 + f0)
            # and also ensuring that it's not more than the maximum possible (which is the number of types)
            max_possible = min(f1 + f0, len(used) + 1)
            for cnt in range(min(f1 + f0, len(used) + 1), 0, -1):
                if cnt not in used:
                    used.add(cnt)
                    total += cnt
                    total_f1 += cnt * (f1 / (f1 + f0))  # approximate, but we'll adjust later
                    break
        
        results.append(f"{total} {int(total_f1)}")
    
    print("\n".join(results))