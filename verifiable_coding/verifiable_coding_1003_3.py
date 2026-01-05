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
        M = int(data[idx+1])
        idx += 2
        
        soints = []
        for _ in range(N):
            Ci = int(data[idx])
            Li = int(data[idx+1])
            soints.append((Ci, Li))
            idx += 2
        
        sofloats = []
        for _ in range(M):
            Ci = int(data[idx])
            Li = int(data[idx+1])
            sofloats.append((Ci, Li))
            idx += 2
        
        # Group by level
        soint_levels = {}
        for Ci, Li in soints:
            if Li not in soint_levels:
                soint_levels[Li] = []
            soint_levels[Li].append(Ci)
        
        sofloat_levels = {}
        for Ci, Li in sofloats:
            if Li not in sofloat_levels:
                sofloat_levels[Li] = []
            sofloat_levels[Li].append(Ci)
        
        # For each level, find the minimum required chakra for soints
        total = 0
        for level in soint_levels:
            soint_powers = soint_levels[level]
            sofloat_powers = sofloat_levels[level]
            
            # Find the maximum sofloat power at this level
            max_so_float = max(sofloat_powers)
            
            # Find the minimum soint power at this level
            min_soin = min(soint_powers)
            
            # The soint must have at least max_so_float + 1 power to win
            # So the required chakra is (max_so_float + 1 - min_soin)
            required = max(0, max_so_float + 1 - min_soin)
            total += required
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()