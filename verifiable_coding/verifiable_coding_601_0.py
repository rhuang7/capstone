import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    events = []
    idx = 1
    for _ in range(N):
        S = int(data[idx])
        D = int(data[idx+1])
        events.append((S, D))
        idx += 2

    events.sort(key=lambda x: (x[0], x[1]))

    count = 0
    last_end = 0

    for s, d in events:
        if s > last_end:
            count += 1
            last_end = s + d

    print(count)

if __name__ == '__main__':
    solve()