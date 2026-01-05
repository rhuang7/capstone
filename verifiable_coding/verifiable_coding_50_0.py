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
        a = list(map(int, data[idx:idx + 2 * n]))
        idx += 2 * n
        
        total_s = a.count(1)
        total_b = a.count(2)
        
        if total_s == total_b:
            results.append(0)
            continue
        
        s = total_s
        b = total_b
        
        left = 0
        right = 0
        left_s = 0
        left_b = 0
        right_s = 0
        right_b = 0
        
        for i in range(2 * n):
            if i < n:
                left_s += a[i] == 1
                left_b += a[i] == 2
            else:
                right_s += a[i] == 1
                right_b += a[i] == 2
        
        s_left = left_s
        b_left = left_b
        s_right = right_s
        b_right = right_b
        
        min_jars = float('inf')
        
        for i in range(n + 1):
            s_remaining = s - i
            b_remaining = b - (n - i)
            
            if s_remaining == b_remaining:
                min_jars = min(min_jars, i + (n - i))
        
        results.append(str(min_jars))
    
    print('\n'.join(results))