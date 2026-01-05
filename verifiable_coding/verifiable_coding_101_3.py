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
        left = c - r
        right = c + r
        
        # Find the intersection of the path [start, end] and the coverage [left, right]
        # The part of the path not in coverage is the total length minus the overlap
        # Calculate the overlap
        overlap_start = max(start, left)
        overlap_end = min(end, right)
        
        if overlap_start >= overlap_end:
            # No overlap, entire path is outside coverage
            total_time = end - start
        else:
            # Part of the path is in coverage
            covered_time = overlap_end - overlap_start
            total_time = end - start - covered_time
        
        results.append(str(total_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()