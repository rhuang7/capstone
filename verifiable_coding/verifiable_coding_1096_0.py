import sys

def solve():
    import bisect

    data = sys.stdin.buffer.read().split()
    ptr = 0

    N = int(data[ptr])
    X = int(data[ptr+1])
    Y = int(data[ptr+2])
    ptr += 3

    contests = []
    for _ in range(N):
        S = int(data[ptr])
        E = int(data[ptr+1])
        contests.append((S, E))
        ptr += 2

    V = list(map(int, data[ptr:ptr+X]))
    ptr += X
    W = list(map(int, data[ptr:ptr+Y]))
    ptr += Y

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
            if w_idx < len(W):
                w_time = W[w_idx]

                total_time = w_time - v_time + 1
                if total_time < min_time:
                    min_time = total_time

    print(min_time)

if __name__ == '__main__':
    solve()