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
        # The part of the path not in coverage is the total length minus the length of intersection
        # If the path is completely outside the coverage, the answer is the full length
        
        # Calculate the length of the path
        path_length = end - start
        
        # Calculate the overlap between [start, end] and [left, right]
        overlap_start = max(start, left)
        overlap_end = min(end, right)
        
        if overlap_start < overlap_end:
            covered_length = overlap_end - overlap_start
        else:
            covered_length = 0
        
        # The time not in coverage is the total path length minus the covered length
        result = path_length - covered_length
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()