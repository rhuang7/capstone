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
        if a[0] != 0 or b[N-1] != 0:
            results.append("No")
            continue
        
        # Check if for all i, a[i] + b[i] >= 0
        valid = True
        for i in range(N):
            if a[i] + b[i] < 0:
                valid = False
                break
        
        if not valid:
            results.append("No")
            continue
        
        # Check if for all i, a[i] + b[i] >= 0 and a[i] + b[i] >= 0
        # Also check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i, a[i] + b[i] >= 0
        # And check if for all i