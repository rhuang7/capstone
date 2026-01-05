import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        C = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Check if the target color can be achieved with the brush
        # The brush can paint 3 consecutive millimeters at a time
        # So, the target must be achievable by overlapping 3-length segments
        
        # Check if the first 3 elements are the same as the first 3 of the target
        # and the last 3 elements are the same as the last 3 of the target
        # and the middle elements can be covered by overlapping segments
        
        # We can only paint 3-length segments, so the target must be such that
        # each position is covered by at least one 3-length segment
        # and the color at each position must be the same as the color of the segment it is covered by
        
        # So, for each position i (0-based), there must be at least one segment [j, j+2] that covers i
        # and the color at i must be equal to the color of that segment
        
        # The segments can be:
        # [0,2], [1,3], [2,4], ..., [N-3, N-1]
        
        # So for each position i, there must be at least one segment that covers it
        # and the color at i must be equal to the color of that segment
        
        # We can check this by ensuring that for each position i, there exists a segment [j, j+2] that covers i
        # and C[i] == C[j]
        
        # So, for each position i, there must be at least one j in [max(0, i-2), min(N-3, i)] such that C[i] == C[j]
        
        # We can precompute for each position i the possible j's and check if any of them have C[i] == C[j]
        
        # But for large N, this would be O(N^2), which is too slow
        
        # So we need a more efficient way
        
        # We can check if the first 3 elements are the same as the first 3 of the target
        # and the last 3 elements are the same as the last 3 of the target
        # and the middle elements can be covered by overlapping segments
        
        # So, check if the first 3 elements are the same as the first 3 of the target
        if C[0] != C[1] or C[0] != C[2]:
            results.append("No")
            continue
        
        # Check if the last 3 elements are the same as the last 3 of the target
        if C[-1] != C[-2] or C[-1] != C[-3]:
            results.append("No")
            continue
        
        # Now check the middle elements
        # For each position i from 3 to N-4, check if there is a segment that covers it
        # and the color at i is the same as the color of that segment
        
        # We can check for each i in 3 to N-4:
        # if there is a j in [max(0, i-2), min(N-3, i)] such that C[i] == C[j]
        
        # To optimize, we can check for each i in 3 to N-4:
        # if C[i] == C[i-2] or C[i] == C[i-1] or C[i] == C[i-3]
        
        # Because the segment [i-2, i] covers i, and the segment [i-1, i+1] covers i, etc.
        
        # So for each i in 3 to N-4, check if C[i] == C[i-2] or C[i] == C[i-1] or C[i] == C[i-3]
        
        valid = True
        for i in range(3, N-3):
            if C[i] != C[i-2] and C[i] != C[i-1] and C[i] != C[i-3]:
                valid = False
                break
        
        if valid:
            results.append("Yes")
        else:
            results.append("No")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()