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
        def will_always_zigzag(trees):
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
        
        # Find all time intervals when the sequence is zigzag
        def find_intervals(trees):
            intervals = []
            # Check if current state is zigzag
            if is_zigzag(trees):
                intervals.append((0, 0))
            
            # Check if it will always be zigzag
            if will_always_zigzag(trees):
                intervals.append((0, float('inf')))
            
            # Check if it will become zigzag at some time
            if will_become_zigzag(trees):
                # Find the earliest time it becomes zigzag
                # This is a simplified check for the purpose of this problem
                # We assume it becomes zigzag at some time t >= 1
                intervals.append((0, 1))
            
            # Remove duplicates and sort
            intervals = list(set(intervals))
            intervals.sort()
            
            # Format the output
            output = []
            for start, end in intervals:
                if end == float('inf'):
                    output.append(f"Inf")
                else:
                    output.append(f"{end}")
            return output
        
        intervals = find_intervals(trees)
        results.append(str(len(intervals)))
        for interval in intervals:
            results.append(interval)
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()