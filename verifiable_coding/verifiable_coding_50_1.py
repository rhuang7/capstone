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
        
        left = []
        right = []
        for i in range(2 * n):
            if a[i] == 1:
                left.append(1)
            else:
                left.append(0)
        
        for i in range(2 * n - 1, -1, -1):
            if a[i] == 1:
                right.append(1)
            else:
                right.append(0)
        
        s = 0
        b = 0
        res = float('inf')
        for i in range(2 * n + 1):
            if i <= n:
                s += left[i]
                b += right[i]
            else:
                s += right[i]
                b += left[i]
            
            if s == b:
                res = min(res, i)
        
        results.append(res)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()