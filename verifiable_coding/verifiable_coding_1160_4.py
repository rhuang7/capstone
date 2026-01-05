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
        def is_zigzag():
            for i in range(1, n):
                if i % 2 == 1:
                    if trees[i][0] <= trees[i-1][0]:
                        return False
                else:
                    if trees[i][0] >= trees[i-1][0]:
                        return False
            return True
        
        # Check if the sequence will be zigzag in the future
        def will_be_zigzag():
            for i in range(1, n):
                if i % 2 == 1:
                    if trees[i][0] <= trees[i-1][0]:
                        return False
                else:
                    if trees[i][0] >= trees[i-1][0]:
                        return False
            return True
        
        # Check if the sequence will be zigzag forever
        def will_be_forever():
            for i in range(1, n):
                if i % 2 == 1:
                    if trees[i][1] <= trees[i-1][1]:
                        return False
                else:
                    if trees[i][1] >= trees[i-1][1]:
                        return False
            return True
        
        # Find all time intervals where the sequence is zigzag
        intervals = []
        if is_zigzag():
            intervals.append((0, 0))
        
        # Check for future intervals
        if will_be_zigzag():
            # Check if it will be forever
            if will_be_forever():
                intervals.append((0, float('inf')))
            else:
                # Find the last time it is zigzag
                last_time = 0
                while True:
                    last_time += 1
                    # Check if the sequence is zigzag at last_time
                    valid = True
                    for i in range(1, n):
                        h1 = trees[i-1][0] + trees[i-1][1] * last_time
                        h2 = trees[i][0] + trees[i][1] * last_time
                        if i % 2 == 1:
                            if h1 <= h2:
                                valid = False
                                break
                        else:
                            if h1 >= h2:
                                valid = False
                                break
                    if valid:
                        last_time += 1
                    else:
                        break
                intervals.append((0, last_time - 1))
        
        # Output the results
        results.append(str(len(intervals)))
        for start, end in intervals:
            if end == float('inf'):
                results.append(f"{start} Inf")
            else:
                results.append(f"{start} {end}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()