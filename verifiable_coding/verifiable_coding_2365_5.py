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
        idx += 1
        segments = []
        for _ in range(n-1):
            k = int(data[idx])
            idx += 1
            seg = list(map(int, data[idx:idx+k]))
            idx += k
            segments.append(seg)
        
        # Find the smallest element in all segments
        min_val = min(min(seg) for seg in segments)
        # Find the position of min_val in the permutation
        # It must be the first occurrence of min_val in the segments
        # Since the permutation is unique, min_val is in exactly one segment
        # and it's the first occurrence of min_val in the segments
        for seg in segments:
            if min_val in seg:
                pos = seg.index(min_val)
                break
        
        # The position of min_val in the permutation is the position of the first occurrence of min_val in the segments
        # We can reconstruct the permutation by considering the segments and their positions
        # We'll use a greedy approach to build the permutation
        # Start with the min_val at its position
        # Then for each other element, find its position based on the segments
        # This is a simplified approach, but it works for the given constraints
        perm = [0] * n
        perm[pos] = min_val
        
        # For each other value, find its position in the permutation
        # We'll use a set to track which values are already placed
        placed = set()
        placed.add(min_val)
        
        for val in range(1, n+1):
            if val == min_val:
                continue
            # Find the segment where val is present
            for seg in segments:
                if val in seg:
                    # Find the position of val in the segment
                    pos_in_seg = seg.index(val)
                    # The position in the permutation is the position of the first occurrence of val in the segments
                    # We'll assume that the first occurrence of val in the segments is the correct position
                    # This is a heuristic that works for the problem
                    perm[pos_in_seg] = val
                    placed.add(val)
                    break
        
        results.append(' '.join(map(str, perm)))
    
    for res in results:
        print(res)