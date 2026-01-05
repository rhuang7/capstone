import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    for _ in range(T):
        S = int(input[idx])
        N = int(input[idx+1])
        K = int(input[idx+2])
        R = int(input[idx+3])
        idx += 4
        
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
    
    if total_required <= sum(int(line.split()[-1]) for line in results if not line.startswith("IMPOSSIBLE")):
        results.append("POSSIBLE")
    else:
        results.append("IMPOSSIBLE")
    
    for line in results:
        print(line)

if __name__ == '__main__':
    solve()