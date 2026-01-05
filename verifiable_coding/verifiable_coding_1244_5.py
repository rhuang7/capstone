import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    events = []
    index = 1
    for _ in range(n):
        b = int(data[index])
        d = int(data[index + 1])
        index += 2
        events.append((b, 1))
        events.append((d, -1))
    
    events.sort()
    res = 0
    current_passengers = 0
    prev = -float('inf')
    for event in events:
        if prev != -float('inf'):
            delta = event[0] - prev
            res = (res + delta * current_passengers) % MOD
        prev = event[0]
        current_passengers += event[1]
    
    print(res % MOD)

if __name__ == '__main__':
    solve()