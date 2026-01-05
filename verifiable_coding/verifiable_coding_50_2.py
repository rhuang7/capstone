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
                right.append(0)
            else:
                left.append(0)
                right.append(1)
        
        s = 0
        b = 0
        res = 0
        for i in range(2 * n):
            if s < total_s and b < total_b:
                if left[i] == 1:
                    s += 1
                else:
                    b += 1
                res += 1
            else:
                break
        
        results.append(res)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    solve()