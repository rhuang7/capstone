import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    events = []
    idx = 1
    for _ in range(n):
        b = int(data[idx])
        d = int(data[idx+1])
        idx += 2
        events.append((b, 1))
        events.append((d, -1))
    
    events.sort()
    res = 0
    current_passengers = 0
    prev = None
    for event in events:
        if prev is not None and prev != event[0]:
            res += (event[0] - prev) * current_passengers
            res %= MOD
        prev = event[0]
        current_passengers += event[1]
    
    print(res % MOD)

if __name__ == '__main__':
    solve()