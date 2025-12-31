import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        a.sort()
        total = sum(a)
        if total > k:
            results.append(0)
            continue
        
        max_ops = 0
        for i in range(n-1, -1, -1):
            if a[i] == 0:
                continue
            cnt = 0
            temp = a[i]
            while True:
                if temp > k:
                    break
                cnt += 1
                temp += a[i]
            max_ops += cnt - 1
        
        results.append(max_ops)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()