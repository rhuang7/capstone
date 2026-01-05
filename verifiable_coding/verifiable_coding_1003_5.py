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
        
        soint = []
        for _ in range(N):
            Ci = int(data[idx])
            Li = int(data[idx+1])
            soint.append((Ci, Li))
            idx += 2
        
        sofloat = []
        for _ in range(M):
            Ci = int(data[idx])
            Li = int(data[idx+1])
            sofloat.append((Ci, Li))
            idx += 2
        
        from collections import defaultdict
        s_level = defaultdict(list)
        f_level = defaultdict(list)
        
        for c, l in soint:
            s_level[l].append(c)
        for c, l in sofloat:
            f_level[l].append(c)
        
        total = 0
        for l in s_level:
            s_list = s_level[l]
            f_list = f_level[l]
            s_list.sort()
            f_list.sort()
            
            # For each level, we need to ensure that the Soint can defeat the Sofloat
            # in the worst case scenario, where the Sofloat has the highest possible power
            # and the Soint has the lowest possible power
            # So we need to make sure that for each Sofloat in this level, the Soint has enough power
            # to defeat it
            # We can do this by making the Soint with the lowest power in this level have enough
            # power to defeat the Sofloat with the highest power in this level
            # So we find the minimum required power for the Soint in this level
            # and calculate the required increase
            required = 0
            for f in f_list:
                if s_list[0] < f:
                    required = f - s_list[0]
                    break
            total += required
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()