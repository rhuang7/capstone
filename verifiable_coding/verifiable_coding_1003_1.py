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
        for ci, li in soints:
            if li not in soint_levels:
                soint_levels[li] = []
            soint_levels[li].append(ci)
        
        sofloat_levels = {}
        for ci, li in sofloats:
            if li not in sofloat_levels:
                sofloat_levels[li] = []
            sofloat_levels[li].append(ci)
        
        # For each level, find the minimal required increase for soints
        total = 0
        for level in soint_levels:
            soint_powers = soint_levels[level]
            sofloat_powers = sofloat_levels[level]
            
            # Find the minimal required power for soints
            # Soint must have power >= max(sofloat_powers)
            # But we can choose to increase soint_powers to match the max of sofloat_powers
            # So the minimal increase is max(0, max(sofloat_powers) - min(soint_powers))
            # But we need to make sure that soint_powers can be increased to at least max(sofloat_powers)
            # So the minimal increase is max(0, max(sofloat_powers) - min(soint_powers))
            # Wait, no. For each soint, we need to make sure that it can beat the sofloats at that level
            # So the minimal required for soint is max(sofloat_powers)
            # So we need to increase the soint with the minimal power to reach max(sofloat_powers)
            # So the minimal increase is max(0, max(sofloat_powers) - min(soint_powers))
            # Because we can increase the soint with the minimal power to reach the max of sofloats
            # This way, all soints can beat the sofloats at that level
            max_sofloat = max(sofloat_powers)
            min_soint = min(soint_powers)
            required = max(0, max_sofloat - min_soint)
            total += required
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()