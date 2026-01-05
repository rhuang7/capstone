import sys

def solve():
    import bisect
    input = sys.stdin.buffer.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    X = int(input[ptr])
    ptr += 1
    Y = int(input[ptr])
    ptr += 1

    contests = []
    for _ in range(N):
        S = int(input[ptr])
        ptr += 1
        E = int(input[ptr])
        ptr += 1
        contests.append((S, E))

    V = list(map(int, input[ptr:ptr+X]))
    ptr += X
    W = list(map(int, input[ptr:ptr+Y]))
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