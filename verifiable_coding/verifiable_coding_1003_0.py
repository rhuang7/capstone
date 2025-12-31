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
        
        from collections import defaultdict
        level_soints = defaultdict(list)
        level_sofloats = defaultdict(list)
        
        for ci, li in soints:
            level_soints[li].append(ci)
        for ci, li in sofloats:
            level_sofloats[li].append(ci)
        
        level_soint_set = set(level_soints.keys())
        level_sofloat_set = set(level_sofloats.keys())
        
        # For each level, we need to ensure that the Soint can defeat the Sofloat
        # We need to find the minimum required chakra for each level
        required = {}
        for level in level_soint_set:
            if level not in level_sofloat_set:
                continue
            s_list = level_soints[level]
            f_list = level_sofloats[level]
            
            # For each Soint, we need to find the minimum required chakra such that
            # it can defeat all Sofloats at this level
            # We take the maximum of (f + 1) for all f in f_list
            # Because if a Soint has chakra c, then c must be > f for all f in f_list
            # So c must be at least (max(f) + 1)
            max_f = max(f_list)
            required[level] = max_f + 1
        
        # Now, for each Soint, we need to calculate how much additional chakra is needed
        # to reach the required chakra for their level
        total = 0
        for ci, li in soints:
            if li not in required:
                continue
            needed = required[li]
            total += max(0, needed - ci)
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()