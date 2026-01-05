import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        R = int(data[idx])
        C = int(data[idx+1])
        M = int(data[idx+2])
        K = int(data[idx+3])
        J = int(data[idx+4])
        idx += 5
        
        total = R * C
        if M + K + J != total:
            results.append("No")
            continue
        
        def get_possible_areas(r, c):
            areas = set()
            for i in range(1, r + 1):
                areas.add(i * c)
            for i in range(1, c + 1):
                areas.add(r * i)
            return areas
        
        possible_m = get_possible_areas(R, C)
        if M not in possible_m:
            results.append("No")
            continue
        
        remaining = total - M
        possible_kj = get_possible_areas(R, C)
        possible_k = set()
        possible_j = set()
        for a in possible_kj:
            if a <= remaining:
                possible_k.add(a)
                possible_j.add(remaining - a)
            else:
                continue
        
        found = False
        for k in possible_k:
            if (K == k) and (J == (remaining - k)):
                found = True
                break
        
        if found:
            results.append("Yes")
        else:
            results.append("No")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()