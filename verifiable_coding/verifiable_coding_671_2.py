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
        N, S = int(data[idx]), int(data[idx+1])
        idx += 2
        P = list(map(int, data[idx:idx+N]))
        idx += N
        pos = list(map(int, data[idx:idx+N]))
        idx += N
        defenders = []
        forwards = []
        for i in range(N):
            if pos[i] == 0:
                defenders.append(P[i])
            else:
                forwards.append(P[i])
        min_def = min(defenders)
        min_forw = min(forwards)
        if S + min_def + min_forw <= 100:
            results.append("yes")
        else:
            results.append("no")
    print('\n'.join(results))