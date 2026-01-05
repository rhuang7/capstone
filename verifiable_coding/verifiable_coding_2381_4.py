import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        n = len(s)
        max_d = 0
        
        # Find the farthest R to the left of the first L
        first_L = -1
        for i in range(n):
            if s[i] == 'L':
                first_L = i
                break
        
        # If there is no L, then the frog can jump directly to the end
        if first_L == -1:
            results.append(n + 1)
            continue
        
        # Find the farthest R to the right of the first L
        last_R = -1
        for i in range(n-1, -1, -1):
            if s[i] == 'R':
                last_R = i
                break
        
        # The minimum d is the distance between the first L and the last R
        max_d = last_R - first_L
        
        # Also, the frog must be able to jump from 0 to the first L, and from the last R to n+1
        # So we need to take the maximum of these distances
        max_d = max(max_d, first_L, n + 1 - last_R)
        
        results.append(str(max_d))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()