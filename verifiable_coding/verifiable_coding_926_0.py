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
        
        for i in range(N - 1):
            max1 = a[i]
            max2 = a[i + 1]
            if max1 < max2:
                max1, max2 = max2, max1
            if max1 + max2 <= k:
                current = 2
                j = i + 1
                while j < N:
                    next_val = a[j]
                    if next_val > max1:
                        max2 = max1
                        max1 = next_val
                    elif next_val > max2:
                        max2 = next_val
                    if max1 + max2 <= k:
                        current += 1
                        j += 1
                    else:
                        break
                if current > max_len:
                    max_len = current
        
        results.append(str(max_len))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()