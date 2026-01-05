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
        
        # The path is from a to b
        # The coverage area is from c - r to c + r
        # Find the overlap between the path and the coverage area
        # The total length of the path is |a - b|
        total_length = abs(a - b)
        
        # The coverage area starts at start_c and ends at end_c
        start_c = c - r
        end_c = c + r
        
        # Find the intersection of [a, b] and [start_c, end_c]
        # The start of the overlap is max(a, start_c)
        # The end of the overlap is min(b, end_c)
        overlap_start = max(a, start_c)
        overlap_end = min(b, end_c)
        
        # If there is no overlap, the entire path is outside coverage
        if overlap_start >= overlap_end:
            print(total_length)
            continue
        
        # The length of the path inside coverage is overlap_end - overlap_start
        coverage_length = overlap_end - overlap_start
        # The time outside coverage is total_length - coverage_length
        print(total_length - coverage_length)

if __name__ == '__main__':
    solve()