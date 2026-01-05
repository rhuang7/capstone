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

    # Use greedy algorithm to select maximum non-overlapping events
    # with at least one gap day between them
    count = 0
    last_end = -1

    for S, D in events:
        start = S
        end = S + D - 1  # end date of the event

        # Check if the current event can be scheduled
        if start > last_end + 1:
            count += 1
            last_end = end

    print(count)

if __name__ == '__main__':
    solve()