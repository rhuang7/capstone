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
        
        # Sort events by preferred room
        for s, e, p in events:
            # Check if the preferred room is available
            # Use greedy algorithm to check if the event can be scheduled
            # Sort intervals by end time
            intervals = room_intervals[p]
            # Check if the new interval can be added without overlap
            # Sort intervals by end time
            intervals.sort()
            can_add = True
            for start, end in intervals:
                if not (e <= start or s >= end):
                    can_add = False
                    break
            if can_add:
                intervals.append((s, e))
                # Sort again after adding to maintain order
                intervals.sort()
        
        # Count total events
        total = 0
        for intervals in room_intervals:
            total += len(intervals)
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()