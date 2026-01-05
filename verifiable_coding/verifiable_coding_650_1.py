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
        # For each room, keep track of intervals that are currently occupied
        room_intervals = [ [] for _ in range(K+1) ]  # rooms are 1-based
        # Sort events by their preferred room
        for s, e, p in events:
            # Check if the room is available
            available = True
            for (start, end) in room_intervals[p]:
                if not (e <= start or s >= end):
                    available = False
                    break
            if available:
                # Add the event to the room's intervals
                room_intervals[p].append((s, e))
                # Sort the intervals by end time to facilitate greedy scheduling
                room_intervals[p].sort(key=lambda x: x[1])
        # Count the total number of events that can be scheduled
        total = 0
        for room in room_intervals:
            total += len(room)
        results.append(str(total))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()