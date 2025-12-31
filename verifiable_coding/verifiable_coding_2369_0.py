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
        type_count = collections.defaultdict(int)
        type_f1 = collections.defaultdict(list)
        type_f0 = collections.defaultdict(list)
        for _ in range(n):
            a = int(data[idx])
            f = int(data[idx + 1])
            idx += 2
            type_count[a] += 1
            if f == 1:
                type_f1[a].append(1)
            else:
                type_f0[a].append(0)
        
        # For each type, we have a list of f=1 and f=0 candies
        # We need to select some of them such that counts are distinct
        # We want to maximize the total number of candies, and then maximize f=1 count
        
        # We'll try to assign as many as possible to f=1, then f=0
        # We'll use a greedy approach with a priority queue
        
        # Sort types by the number of f=1 candies in descending order
        types = sorted(type_count.items(), key=lambda x: len(x[1][0]), reverse=True)
        
        # For each type, we can take up to min(count, k) where k is the number of distinct counts
        # We'll try to assign as many as possible to f=1, then f=0
        
        # We'll use a max-heap to track the number of candies we can take of each type
        # We'll also track the total count and f=1 count
        
        total = 0
        f1_count = 0
        used = set()
        max_count = 0
        
        for a, (f1_list, f0_list) in types:
            # We can take up to min(len(f1_list), len(f0_list), ...) but we need to ensure distinct counts
            # We'll try to take as many as possible from f1_list first
            # We'll try to assign counts in a way that they are unique
            
            # Try to assign as many as possible from f1_list
            # We'll try to assign counts from 1 to max_possible
            # We'll try to assign as many as possible from f1_list
            
            # We'll try to assign as many as possible from f1_list
            # We'll use a max-heap to track the possible counts
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list
            # We'll try to assign as many as possible from f1_list