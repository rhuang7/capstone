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
        
        s = 0
        b = 0
        left = 0
        right = 2 * n - 1
        min_jars = float('inf')
        
        while left <= right:
            if a[left] == 1:
                s += 1
            else:
                b += 1
            if a[right] == 1:
                s += 1
            else:
                b += 1
            if s == b:
                min_jars = min(min_jars, (left + 1) + (2 * n - right))
            left += 1
            right -= 1
        
        results.append(min_jars)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()