import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        S = int(data[index])
        N = int(data[index+1])
        K = int(data[index+2])
        R = int(data[index+3])
        index += 4
        
        total = 0
        current = K
        for _ in range(N):
            total += current
            current *= R
        
        if total <= S:
            results.append(f"POSSIBLE {S - total}")
        else:
            results.append(f"IMPOSSIBLE {total - S}")
    
    # Calculate total slices needed for all families
    total_slices_needed = 0
    for i in range(T):
        S = int(data[1 + 4*i])
        N = int(data[2 + 4*i])
        K = int(data[3 + 4*i])
        R = int(data[4 + 4*i])
        current = K
        total = 0
        for _ in range(N):
            total += current
            current *= R
        total_slices_needed += total
    
    # Calculate total slices available
    total_slices_available = 0
    for i in range(T):
        total_slices_available += int(data[1 + 4*i])
    
    if total_slices_available >= total_slices_needed:
        results.append("POSSIBLE")
    else:
        results.append("IMPOSSIBLE")
    
    for line in results:
        print(line)