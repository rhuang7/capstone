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
        N, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_len = 2
        for i in range(N-1):
            max1 = a[i]
            max2 = a[i+1]
            if max1 < max2:
                max1, max2 = max2, max1
            if max1 + max2 <= k:
                current = 2
                for j in range(i+2, N):
                    val = a[j]
                    if val > max1:
                        max2 = max1
                        max1 = val
                    elif val > max2:
                        max2 = val
                    if max1 + max2 <= k:
                        current += 1
                        max_len = max(max_len, current)
                    else:
                        break
                if max1 + max2 <= k:
                    max_len = max(max_len, current)
        
        results.append(str(max_len))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()