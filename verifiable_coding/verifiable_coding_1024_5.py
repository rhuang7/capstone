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
        
        # Calculate required slices for the family
        total = 0
        current = K
        for _ in range(N):
            total += current
            current *= R
        
        if total <= S:
            results.append(f"POSSIBLE {S - total}")
        else:
            results.append(f"IMPOSSIBLE {total - S}")
    
    # Calculate total slices and total required for sharing
    total_slices = sum(int(s.split()[0]) for s in results)
    total_required = sum(int(s.split()[1]) for s in results)
    
    if total_slices >= total_required:
        results.append("POSSIBLE")
    else:
        results.append("IMPOSSIBLE")
    
    for line in results:
        print(line)

if __name__ == '__main__':
    solve()