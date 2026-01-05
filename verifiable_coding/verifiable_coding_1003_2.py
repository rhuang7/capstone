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
        
        sofloods = []
        for _ in range(M):
            Ci = int(data[idx])
            Li = int(data[idx+1])
            sofloods.append((Ci, Li))
            idx += 2
        
        # Group by level
        s_level = {}
        s_power = {}
        for ci, li in soints:
            if li not in s_level:
                s_level[li] = []
                s_power[li] = []
            s_level[li].append(ci)
            s_power[li].append(ci)
        
        f_level = {}
        f_power = {}
        for ci, li in sofloods:
            if li not in f_level:
                f_level[li] = []
                f_power[li] = []
            f_level[li].append(ci)
            f_power[li].append(ci)
        
        # For each level, find the minimum required chakra for Soints
        total = 0
        for level in s_level:
            s_powers = s_level[level]
            f_powers = f_level[level]
            
            # Find the minimum required chakra for Soints at this level
            # So that for all Sofloats at this level, Soint's power >= Sofloat's power
            # After adding chakra, Soint's power >= Sofloat's power
            # So the required chakra for Soint is max(0, (max_f_power - min_s_power))
            # But we need to ensure that for all Sofloats at this level, Soint's power >= Sofloat's power
            # So the required chakra for Soint is max(0, (max_f_power - min_s_power))
            # But we need to choose the Soint with the minimum power to ensure that all Sofloats are handled
            # So we take the minimum Soint power and compare with max Sofloat power
            min_s = min(s_powers)
            max_f = max(f_powers)
            required = max(0, max_f - min_s)
            total += required
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()