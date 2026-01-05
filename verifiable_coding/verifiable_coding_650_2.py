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
        room_intervals = [ [] for _ in range(K+1) ]  # rooms are 1-based
        
        # Sort events by their preferred room
        for s, e, p in events:
            # Check if the preferred room is available
            # Use greedy algorithm to check if the interval can be added
            # Sort the intervals in the room by end time
            intervals = room_intervals[p]
            # Check if the new interval can be added
            can_add = True
            for (start, end) in intervals:
                if not (e <= start or s >= end):
                    can_add = False
                    break
            if can_add:
                # Add the interval to the room
                intervals.append((s, e))
                # Sort the intervals by end time
                intervals.sort(key=lambda x: x[1])
        
        # Count the total number of events that can be scheduled
        total = 0
        for intervals in room_intervals:
            total += len(intervals)
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()