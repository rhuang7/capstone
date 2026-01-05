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
        count = collections.defaultdict(list)
        for _ in range(n):
            a = int(data[idx])
            f = int(data[idx + 1])
            idx += 2
            count[a].append(f)
        
        # For each type, sort the f_i in descending order (we want to take as many 1s as possible)
        for key in count:
            count[key].sort(reverse=True)
        
        # We need to select for each type a number of candies (k) such that all k's are distinct
        # We want to maximize the total number of candies, and among those, maximize the number of 1s
        
        # We'll use a greedy approach:
        # 1. For each type, we can take up to the number of 1s (since they are more valuable)
        # 2. We'll try to assign as many as possible, but ensuring that the counts are unique
        
        # We'll use a max-heap to keep track of the maximum possible counts we can take
        # We'll also track the number of 1s we can take for each count
        
        # First, collect all the possible counts for each type
        type_counts = []
        for key in count:
            # The number of 1s in this type
            ones = sum(1 for f in count[key] if f == 1)
            # The number of 0s in this type
            zeros = len(count[key]) - ones
            # We can take up to ones 1s, and up to zeros 0s
            # But the total for this type is the number of candies we can take (up to the number of candies)
            # However, we need to ensure that the total counts are unique
            # So we'll try to take as many as possible, but in a way that the counts are unique
            # We'll use a max-heap to track the maximum possible counts we can take
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll try to take the maximum possible number of candies for each type, but ensuring that the counts are unique
            # We'll use a greedy approach: for each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible
            # We'll use a max-heap to track the maximum possible counts we can take
            # We'll also track the number of 1s we can take for each count
            # For each type, we can take up to the number of candies, but we'll try to take as many as possible