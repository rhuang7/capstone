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
        # For each room, sort events by end time
        room_events = [[] for _ in range(K+1)]
        for s, e, p in events:
            room_events[p].append((s, e))
        # For each room, select maximum number of non-overlapping events
        count = 0
        for room in room_events:
            # Sort by start time
            room.sort()
            # Greedy algorithm: select earliest ending events
            last_end = -1
            for s, e in room:
                if s >= last_end:
                    count += 1
                    last_end = e
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()