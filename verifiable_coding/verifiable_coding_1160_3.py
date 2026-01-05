import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        trees = []
        for _ in range(n):
            h = int(data[idx])
            m = int(data[idx+1])
            trees.append((h, m))
            idx += 2
        
        # Check if the current state is zigzag
        def is_zigzag(trees):
            for i in range(1, n):
                if i % 2 == 1:
                    if trees[i][0] <= trees[i-1][0]:
                        return False
                else:
                    if trees[i][0] >= trees[i-1][0]:
                        return False
            return True
        
        # Check if the sequence will remain zigzag forever
        def is_forever_zigzag(trees):
            for i in range(1, n):
                if i % 2 == 1:
                    if trees[i][1] <= trees[i-1][1]:
                        return False
                else:
                    if trees[i][1] >= trees[i-1][1]:
                        return False
            return True
        
        # Check if the sequence will become zigzag at some time
        def will_become_zigzag(trees):
            for i in range(1, n):
                if i % 2 == 1:
                    if trees[i][1] <= trees[i-1][1]:
                        return False
                else:
                    if trees[i][1] >= trees[i-1][1]:
                        return False
            return True
        
        # Check if the sequence will become zigzag at some time
        def will_become_zigzag_after(trees, t):
            for i in range(1, n):
                if i % 2 == 1:
                    if trees[i][0] + t * trees[i][1] <= trees[i-1][0] + t * trees[i-1][1]:
                        return False
                else:
                    if trees[i][0] + t * trees[i][1] >= trees[i-1][0] + t * trees[i-1][1]:
                        return False
            return True
        
        # Check if the sequence will become zigzag at some time
        def will_become_zigzag_after_time(t):
            for i in range(1, n):
                if i % 2 == 1:
                    if (trees[i][0] - trees[i-1][0]) + t * (trees[i][1] - trees[i-1][1]) <= 0:
                        return False
                else:
                    if (trees[i][0] - trees[i-1][0]) + t * (trees[i][1] - trees[i-1][1]) >= 0:
                        return False
            return True
        
        # Find all time intervals when the sequence is zigzag
        intervals = []
        
        # Check if current state is zigzag
        if is_zigzag(trees):
            intervals.append((0, 0))
        
        # Check if the sequence will become zigzag at some time
        if will_become_zigzag(trees):
            # Find the earliest time when it becomes zigzag
            left = 0
            right = 10**18
            while left < right:
                mid = (left + right) // 2
                if will_become_zigzag_after_time(mid):
                    right = mid
                else:
                    left = mid + 1
            earliest = left
            
            # Check if it will remain zigzag forever
            if is_forever_zigzag(trees):
                intervals.append((earliest, 10**18))
            else:
                # Find the latest time when it remains zigzag
                left = earliest
                right = 10**18
                while left < right:
                    mid = (left + right + 1) // 2
                    if will_become_zigzag_after_time(mid):
                        left = mid
                    else:
                        right = mid - 1
                latest = left
                intervals.append((earliest, latest))
        
        # Output the results
        results.append(str(len(intervals)))
        for start, end in intervals:
            if end == 10**18:
                results.append(f"{start} Inf")
            else:
                results.append(f"{start} {end}")
    
    print('\n'.join(results))