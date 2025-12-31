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

    # Sort events by start date
    events.sort()

    # Greedy algorithm: select events that do not overlap and have at least one gap day
    count = 0
    last_end = -1

    for S, D in events:
        start = S
        end = S + D - 1  # end date of the event (inclusive)
        if start > last_end + 1:
            count += 1
            last_end = end

    print(count)

if __name__ == '__main__':
    solve()