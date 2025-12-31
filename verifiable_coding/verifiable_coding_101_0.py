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
        
        # The coverage interval is [c - r, c + r]
        coverage_start = c - r
        coverage_end = c + r
        
        # Find the intersection of the path with the coverage area
        path_start = min(start, end)
        path_end = max(start, end)
        
        # Find the overlap between the path and the coverage area
        overlap_start = max(path_start, coverage_start)
        overlap_end = min(path_end, coverage_end)
        
        if overlap_start > overlap_end:
            # No overlap, full time is outside
            results.append(path_end - path_start)
        else:
            # Time inside coverage is (overlap_end - overlap_start)
            # Time outside is total time - time inside
            total_time = path_end - path_start
            time_inside = overlap_end - overlap_start
            results.append(total_time - time_inside)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()