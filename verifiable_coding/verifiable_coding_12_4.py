import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Check if a can be transformed into b
        possible = True
        for i in range(n):
            if a[i] != b[i]:
                possible = False
                break
        if possible:
            results.append("YES")
            continue
        
        # Check if a can be transformed into b through operations
        # For each element in b, check if it can be achieved from a[i]
        # Since operations can be done any number of times, we need to check if b[i] can be achieved from a[i]
        # The operations allow adding a[i] to a[j], so the value of b[j] must be achievable through some combination of a[i]s
        # Since a[i] is -1, 0, or 1, we can only add -1, 0, or 1 to a[j]
        # So for each element in b, it must be possible to reach it from a[i] by adding some combination of a[i]s
        # For example, if a[i] is 1, then b[j] can be any number that is equal to a[i] + k*1, where k is an integer
        # So for a[i] = 1, b[j] must be >= a[i] (since we can add 1 multiple times)
        # For a[i] = -1, b[j] must be <= a[i] (since we can add -1 multiple times)
        # For a[i] = 0, b[j] must be equal to a[i] (since adding 0 doesn't change anything)
        
        # Check for each element in b
        for i in range(n):
            ai = a[i]
            bi = b[i]
            if ai == 0:
                if bi != 0:
                    possible = False
                    break
            elif ai == 1:
                if bi < ai:
                    possible = False
                    break
            elif ai == -1:
                if bi > ai:
                    possible = False
                    break
        results.append("YES" if possible else "NO")
    
    print('\n'.join(results))