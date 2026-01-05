import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        r = int(data[index+3])
        index += 4
        
        # Determine the direction of movement
        if a > b:
            a, b = b, a
            direction = -1
        else:
            direction = 1
        
        # Calculate the range of x where Polycarp is in coverage
        start = c - r
        end = c + r
        
        # Find the overlap between the path and the coverage area
        path_start = a
        path_end = b
        
        # Calculate the intersection of the path and coverage
        overlap_start = max(path_start, start)
        overlap_end = min(path_end, end)
        
        # If there is no overlap, the total time is the full path length
        if overlap_start >= overlap_end:
            print(b - a)
            continue
        
        # Calculate the time spent in coverage
        time_in_coverage = overlap_end - overlap_start
        
        # Calculate the total time
        total_time = b - a
        
        # Time not in coverage is total time minus time in coverage
        print(total_time - time_in_coverage)

if __name__ == '__main__':
    solve()