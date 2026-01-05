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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        events = []
        for _ in range(N):
            s = int(data[idx])
            e = int(data[idx+1])
            p = int(data[idx+2])
            events.append((s, e, p))
            idx += 3
        # For each room, keep track of intervals
        room_intervals = [[] for _ in range(K+1)]  # rooms are 1-based
        for s, e, p in events:
            room_intervals[p].append((s, e))
        # For each room, sort intervals by end time
        for i in range(1, K+1):
            room_intervals[i].sort()
        # For each room, try to schedule as many events as possible
        count = 0
        for i in range(1, K+1):
            intervals = room_intervals[i]
            # Use greedy algorithm to schedule as many as possible
            # Sort by start time
            intervals.sort()
            prev_end = 0
            for s, e in intervals:
                if s >= prev_end:
                    count += 1
                    prev_end = e
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()