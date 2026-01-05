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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        if n == 1:
            results.append("Yes")
            continue
        
        increasing = []
        decreasing = []
        for num in a:
            increasing.append(num)
            decreasing.append(num)
        
        for i in range(1, n):
            if increasing[i] <= increasing[i - 1]:
                increasing[i] = increasing[i - 1] - 1
        
        for i in range(n - 2, -1, -1):
            if decreasing[i] <= decreasing[i + 1]:
                decreasing[i] = decreasing[i + 1] + 1
        
        found = False
        for k in range(1, n + 1):
            if increasing[k - 1] > increasing[k - 2] and decreasing[k - 1] > decreasing[k]:
                found = True
                break
        
        results.append("Yes" if found else "No")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()