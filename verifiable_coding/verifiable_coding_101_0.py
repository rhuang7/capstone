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
        # The part of the path not covered is the total length minus the covered part
        # If the coverage is completely outside the path, the entire path is not covered
        
        # Calculate the total path length
        total_length = end - start
        
        # Calculate the covered part
        # The covered part is the overlap between [start, end] and [left, right]
        covered_start = max(start, left)
        covered_end = min(end, right)
        
        if covered_start >= covered_end:
            # No overlap, entire path is not covered
            results.append(total_length)
        else:
            covered_length = covered_end - covered_start
            results.append(total_length - covered_length)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()