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
    total_slices = 0
    total_required = 0
    
    for res in results:
        if res.startswith("IMPOSSIBLE"):
            total_required += int(res.split()[-1])
    
    total_slices = sum(int(res.split()[-1]) for res in results if not res.startswith("IMPOSSIBLE"))
    
    if total_required <= total_slices:
        results.append("POSSIBLE")
    else:
        results.append("IMPOSSIBLE")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()