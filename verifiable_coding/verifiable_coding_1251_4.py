import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    
    idx = 0
    N = int(data[idx])
    idx += 1
    cities = data[idx].split()
    idx += 1
    M = int(data[idx])
    idx += 1
    roads = {}
    for _ in range(M):
        parts = data[idx].split()
        idx += 1
        c1 = parts[0]
        c2 = parts[1]
        d = int(parts[2])
        if c1 not in roads:
            roads[c1] = {}
        roads[c1][c2] = d
    
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        parts = data[idx].split()
        idx += 1
        K = int(parts[0])
        route = parts[1:]
        if K == 1:
            if route[0] in cities:
                results.append('0')
            else:
                results.append('ERROR')
            continue
        
        valid = True
        for i in range(K):
            if route[i] not in cities:
                valid = False
                break
        if not valid:
            results.append('ERROR')
            continue
        
        for i in range(K - 1):
            if route[i] == route[i + 1]:
                valid = False
                break
        if not valid:
            results.append('ERROR')
            continue
        
        for i in range(K - 1):
            if route[i + 1] not in roads.get(route[i], {}):
                valid = False
                break
        if not valid:
            results.append('ERROR')
            continue
        
        total = 0
        for i in range(K - 1):
            total += roads[route[i]][route[i + 1]]
        results.append(str(total))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()