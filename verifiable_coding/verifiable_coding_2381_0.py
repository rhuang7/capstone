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
        d = 0
        
        # Find the first 'R' from the left
        first_r = -1
        for i in range(n):
            if s[i] == 'R':
                first_r = i
                break
        
        # If there is no 'R', the frog must jump directly to n+1
        if first_r == -1:
            results.append(str(n + 1))
            continue
        
        # Find the last 'L' from the right
        last_l = -1
        for i in range(n-1, -1, -1):
            if s[i] == 'L':
                last_l = i
                break
        
        # The minimal d is the maximum of:
        # - distance from 0 to first R
        # - distance from last L to n+1
        d = max(first_r, n - last_l)
        results.append(str(d))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()