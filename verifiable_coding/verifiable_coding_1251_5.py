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
    
    for _ in range(T):
        parts = data[idx].split()
        idx += 1
        K = int(parts[0])
        route = parts[1:]
        
        # Check if all cities in route are valid
        valid = True
        for city in route:
            if city not in cities:
                valid = False
                break
        
        if not valid:
            print("ERROR")
            continue
        
        # Check if consecutive cities are different
        for i in range(K - 1):
            if route[i] == route[i + 1]:
                valid = False
                break
        
        if not valid:
            print("ERROR")
            continue
        
        # Check if first and last city are different
        if route[0] == route[-1]:
            print("ERROR")
            continue
        
        # Check if each consecutive pair has a road
        total = 0
        for i in range(K - 1):
            c1 = route[i]
            c2 = route[i + 1]
            if c1 not in roads or c2 not in roads[c1]:
                valid = False
                break
            total += roads[c1][c2]
        
        if not valid:
            print("ERROR")
        else:
            print(total)
            
if __name__ == '__main__':
    solve()