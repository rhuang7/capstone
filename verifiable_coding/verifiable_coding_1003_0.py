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
        s_level = {}
        s_power = {}
        for c, l in soints:
            if l not in s_level:
                s_level[l] = []
                s_power[l] = []
            s_level[l].append(c)
            s_power[l].append(c)
        
        f_level = {}
        f_power = {}
        for c, l in sofloats:
            if l not in f_level:
                f_level[l] = []
                f_power[l] = []
            f_level[l].append(c)
            f_power[l].append(c)
        
        # For each level, find the minimum required chakra for Soints
        total = 0
        for l in s_level:
            # Get the minimum power of Soints and Sofloats at this level
            min_s = min(s_level[l])
            min_f = min(f_level[l])
            
            # If Soint's power is less than Sofloat's, we need to increase it
            if min_s < min_f:
                total += (min_f - min_s)
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()