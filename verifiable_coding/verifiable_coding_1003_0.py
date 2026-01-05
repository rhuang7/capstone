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
        
        total = 0
        for level in level_soints:
            s_list = level_soints[level]
            f_list = level_sofloats[level]
            
            s = min(s_list)
            f = min(f_list)
            
            if s < f:
                total += (f - s)
            elif s > f:
                pass
            else:
                total += 0
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()