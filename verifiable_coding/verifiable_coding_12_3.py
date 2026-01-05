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
        
        possible = True
        for i in range(n):
            if a[i] != b[i]:
                possible = False
                break
        if not possible:
            results.append("NO")
            continue
        
        # Check if the first element of a is -1, 0, or 1
        # For the rest, check if they can be adjusted
        for i in range(1, n):
            if a[i] == 1:
                if b[i] < 0:
                    possible = False
                    break
            elif a[i] == -1:
                if b[i] > 0:
                    possible = False
                    break
            else:  # a[i] == 0
                if b[i] != 0:
                    possible = False
                    break
        
        results.append("YES" if possible else "NO")
    
    print('\n'.join(results))