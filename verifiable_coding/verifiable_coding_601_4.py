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

    events.sort()
    last_end = 0
    count = 0

    for S, D in events:
        start = S
        end = S + D - 1
        if start > last_end:
            count += 1
            last_end = end

    print(count)

if __name__ == '__main__':
    solve()