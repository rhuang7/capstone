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
        
        # Find the peak position
        peak = 0
        for i in range(1, n):
            if a[i] > a[i - 1]:
                peak = i
            else:
                break
        
        # Check if the array can be made sharpened
        can = True
        # Check increasing part
        for i in range(peak):
            if a[i] >= a[i + 1]:
                can = False
                break
        if not can:
            results.append("No")
            continue
        
        # Check decreasing part
        for i in range(peak, n - 1):
            if a[i] <= a[i + 1]:
                can = False
                break
        if can:
            results.append("Yes")
        else:
            results.append("No")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()