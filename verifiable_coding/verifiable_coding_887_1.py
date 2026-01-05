import sys
import math

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
        a = list(map(float, data[idx:idx+N]))
        idx += N
        b = list(map(float, data[idx:idx+N]))
        idx += N
        
        # Check if a[0] is 0 and b[N-1] is 0
        if abs(a[0] - 0) > 1e-9 or abs(b[N-1] - 0) > 1e-9:
            results.append("No")
            continue
        
        # Check if for all i, a[i] + b[i] >= 0
        valid = True
        for i in range(N):
            if abs(a[i] + b[i]) < 1e-9:
                valid = False
                break
        if not valid:
            results.append("No")
            continue
        
        # Check if for all i, a[i] + b[i] >= 0 and a[i] + b[i] >= a[j] + b[j] for all j < i
        # This is equivalent to checking if a[i] + b[i] is non-decreasing
        # But since we can't have negative distances, we just need to ensure that a[i] + b[i] >= 0
        # and that for all i, a[i] + b[i] >= a[j] + b[j] for j < i
        # So we check if a[i] + b[i] is non-decreasing
        prev = a[0] + b[0]
        for i in range(1, N):
            current = a[i] + b[i]
            if current < prev - 1e-9:
                valid = False
                break
            prev = current
        if not valid:
            results.append("No")
            continue
        
        results.append("Yes")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()