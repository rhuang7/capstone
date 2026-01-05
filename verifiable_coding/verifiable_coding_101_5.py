import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        r = int(data[index+3])
        index += 4
        
        # Determine the direction of movement
        if a > b:
            start, end = b, a
        else:
            start, end = a, b
        
        # Determine the coverage interval
        left = c - r
        right = c + r
        
        # Find the intersection of the path with the coverage area
        # The path is from start to end
        # The coverage is from left to right
        
        # Find the overlap between [start, end] and [left, right]
        overlap_start = max(start, left)
        overlap_end = min(end, right)
        
        # If there is no overlap, the total time is the full path length
        if overlap_start >= overlap_end:
            results.append(end - start)
        else:
            # The time in coverage is (overlap_end - overlap_start)
            # The time not in coverage is (end - start) - (overlap_end - overlap_start)
            results.append((end - start) - (overlap_end - overlap_start))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()