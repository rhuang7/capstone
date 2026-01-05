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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        B = list(map(int, data[idx:idx+N]))
        idx += N
        
        sorted_A = sorted(A)
        sorted_B = sorted(B)
        
        if sorted_A != sorted_B:
            results.append("-1")
            continue
        
        a = sorted(A)
        b = sorted(B)
        
        cost = 0
        i = 0
        j = 0
        while i < N and j < N:
            if a[i] == b[j]:
                i += 1
                j += 1
            elif a[i] < b[j]:
                cost += a[i]
                i += 1
            else:
                cost += b[j]
                j += 1
        
        results.append(str(cost))
    
    print('\n'.join(results))