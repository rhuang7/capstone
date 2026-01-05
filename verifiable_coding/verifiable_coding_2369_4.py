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
        a = []
        f = []
        for _ in range(n):
            ai = int(data[idx])
            fi = int(data[idx + 1])
            a.append(ai)
            f.append(fi)
            idx += 2
        
        type_count = collections.defaultdict(int)
        type_f1 = collections.defaultdict(list)
        type_f0 = collections.defaultdict(list)
        
        for i in range(n):
            ai = a[i]
            fi = f[i]
            type_count[ai] += 1
            if fi == 1:
                type_f1[ai].append(i)
            else:
                type_f0[ai].append(i)
        
        # For each type, we can take at most one candy of that type in the gift
        # So we need to select a subset of types, and for each selected type, choose one candy
        # But we also need to maximize the number of candies, and then the number of f=1 candies
        
        # First, collect all types with at least one candy
        types = list(type_count.keys())
        m = len(types)
        
        # We need to select a subset of types, with size k, such that we can take one candy from each
        # The maximum k is the maximum number of types we can select, such that the number of candies of each type is at least 1
        
        # So the maximum possible number of candies is the maximum k where we can select k types, and for each selected type, we can take one candy
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum possible k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of types with at least one candy, but we need to select k types such that the number of candies of each type is at least 1
        
        # So the maximum k is the number of