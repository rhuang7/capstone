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
        # It must be the first occurrence of min_val in any segment
        pos = -1
        for seg in segments:
            if min_val in seg:
                pos = seg.index(min_val)
                break
        
        # Build the permutation
        p = [0] * n
        p[pos] = min_val
        used = set([min_val])
        
        # Use a greedy approach to fill the rest of the permutation
        # We'll use a priority queue to select the next smallest available number
        from heapq import heappush, heappop
        heap = []
        for seg in segments:
            for num in seg:
                if num not in used:
                    heappush(heap, num)
        
        # Fill the permutation
        for i in range(n):
            if p[i] == 0:
                p[i] = heappop(heap)
        
        results.append(' '.join(map(str, p)) + ' ')
    
    print(''.join(results).strip())

if __name__ == '__main__':
    solve()