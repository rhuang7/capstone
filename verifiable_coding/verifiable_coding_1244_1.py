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
    curr_passengers = 0
    prev_pos = None
    for pos, change in events:
        if prev_pos is not None and prev_pos != pos:
            res += (pos - prev_pos) * curr_passengers
            res %= MOD
        curr_passengers += change
        prev_pos = pos
    
    print(res % MOD)

if __name__ == '__main__':
    solve()