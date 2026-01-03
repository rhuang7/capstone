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
            if not increasing or num > increasing[-1]:
                increasing.append(num)
            else:
                break
        for num in reversed(a):
            if not decreasing or num < decreasing[-1]:
                decreasing.append(num)
            else:
                break
        
        if len(increasing) == n or len(decreasing) == n:
            results.append("Yes")
        else:
            # Try to find a k where the first part is strictly increasing and the second is strictly decreasing
            # We can only do this if the peak is at some position
            # We can try all possible peaks
            found = False
            for k in range(1, n):
                # Check if the first k elements can be strictly increasing
                valid = True
                for i in range(1, k):
                    if a[i] <= a[i - 1]:
                        valid = False
                        break
                if not valid:
                    continue
                # Check if the remaining elements can be strictly decreasing
                for i in range(k, n - 1):
                    if a[i] <= a[i + 1]:
                        valid = False
                        break
                if valid:
                    found = True
                    break
            results.append("Yes" if found else "No")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()