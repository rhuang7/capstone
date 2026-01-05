import sys

def solve():
    import bisect
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    X = int(data[idx+1])
    Y = int(data[idx+2])
    idx += 3
    
    contests = []
    for _ in range(N):
        S = int(data[idx])
        E = int(data[idx+1])
        contests.append((S, E))
        idx += 2
    
    V = list(map(int, data[idx:idx+X]))
    idx += X
    W = list(map(int, data[idx:idx+Y]))
    
    V.sort()
    W.sort()
    
    min_time = float('inf')
    
    for S, E in contests:
        # Find the latest V <= S
        v_idx = bisect.bisect_right(V, S) - 1
        if v_idx >= 0:
            v_time = V[v_idx]
            
            # Find the earliest W >= E
            w_idx = bisect.bisect_left(W, E)
            if w_idx < Y:
                w_time = W[w_idx]
                total_time = w_time - v_time + 1
                if total_time < min_time:
                    min_time = total_time
    
    print(min_time)

if __name__ == '__main__':
    solve()