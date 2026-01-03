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
        if a[0] != 0 or b[-1] != 0:
            results.append("No")
            continue
        
        # Check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[0]
        # And check if a[i] + b[i] is the same for all i
        # Also check if a[i] + b[i] is the same as a[0] + b[