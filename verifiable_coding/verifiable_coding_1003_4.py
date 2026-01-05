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
        s_level = defaultdict(list)
        f_level = defaultdict(list)
        
        for ci, li in soints:
            s_level[li].append(ci)
        
        for ci, li in sofloats:
            f_level[li].append(ci)
        
        required = {}
        for level in s_level:
            if level not in f_level:
                continue
            s_powers = s_level[level]
            f_powers = f_level[level]
            min_s = min(s_powers)
            min_f = min(f_powers)
            if min_s < min_f:
                required[level] = min_f - min_s
            elif min_s > min_f:
                required[level] = 0
            else:
                required[level] = 0
        
        total = sum(required.values())
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()