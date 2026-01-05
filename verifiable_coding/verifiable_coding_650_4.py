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
        # For each room, keep track of intervals that are already booked
        room_intervals = [ [] for _ in range(K+1) ]  # 1-based indexing
        # Sort events by preferred room
        for s, e, p in events:
            # Check if the room is available
            # Use binary search to check if there is an overlapping interval
            intervals = room_intervals[p]
            # Find the first interval with start time >= s
            low, high = 0, len(intervals)
            while low < high:
                mid = (low + high) // 2
                if intervals[mid][1] > s:
                    high = mid
                else:
                    low = mid + 1
            # Check if the new interval overlaps with any before or after
            if low > 0 and intervals[low-1][1] > s:
                # Overlaps with previous
                continue
            if low < len(intervals) and intervals[low][0] > e:
                # Overlaps with next
                continue
            # If no overlap, add the interval
            intervals.append((s, e))
        # Count the total number of events that can be scheduled
        total = 0
        for intervals in room_intervals:
            total += len(intervals)
        results.append(str(total))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()