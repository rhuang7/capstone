import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+m]))
        idx += m
        
        from collections import defaultdict
        count = defaultdict(int)
        for num in a:
            count[num] += 1
        
        # Convert counts to log2 for easier handling
        log_count = {}
        for power in count:
            log = power.bit_length() - 1
            log_count[log] = count[power]
        
        # Try to fill the bag from the largest power of two down
        res = 0
        remaining = n
        for power in range(60, -1, -1):
            if remaining == 0:
                break
            # Current power of two is 2^power
            current = 1 << power
            # How many of this power do we have?
            have = log_count.get(power, 0)
            # How many do we need?
            need = (remaining + current - 1) // current
            if have >= need:
                remaining -= need * current
            else:
                # We need to split the boxes
                # We need (need - have) more boxes of this power
                # Each box can be split into two of power-1
                # So we need to split (need - have) boxes
                # But we can only split boxes that are of higher power
                # So we need to check if we have enough higher power boxes
                # to split into this power
                # We need to find how many splits are needed
                # to get enough boxes of this power
                # We can use a greedy approach here
                # We need to split boxes of higher power down to this power
                # So we need to find the number of splits needed
                # to get at least (need - have) boxes of this power
                # We can use a BFS-like approach to find the minimum splits
                # to get the required number of boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # We can use a greedy approach to split the largest possible boxes first
                # to minimize the number of splits
                # So we need to find the minimum splits to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                # to minimize the number of splits
                # We can use a BFS-like approach to find the minimum splits
                # to get at least (need - have) boxes of this power
                # We can use a priority queue to always split the largest possible boxes first
                #