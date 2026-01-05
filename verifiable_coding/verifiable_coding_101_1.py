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
        
        # Calculate the time Polycarp is in coverage
        # Find the overlap between [path_start, path_end] and [coverage_start, coverage_end]
        overlap_start = max(path_start, coverage_start)
        overlap_end = min(path_end, coverage_end)
        
        if overlap_start > overlap_end:
            # No overlap, time in coverage is 0
            in_coverage_time = 0
        else:
            in_coverage_time = overlap_end - overlap_start
        
        # Total time of the journey
        total_time = path_end - path_start
        
        # Time not in coverage
        results.append(total_time - in_coverage_time)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()