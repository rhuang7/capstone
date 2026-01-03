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
        
        # Check if the sequence will remain zigzag forever
        def is_forever_zigzag():
            for i in range(1, n):
                if i % 2 == 1:
                    # Should be decreasing
                    if trees[i][1] <= trees[i-1][1]:
                        return False
                else:
                    # Should be increasing
                    if trees[i][1] >= trees[i-1][1]:
                        return False
            return True
        
        # Check if the sequence will become zigzag at some time t
        def check_future():
            # We need to find all t >= 0 where the sequence is zigzag
            # We can model the sequence as a function of time
            # For each pair of consecutive trees, we can find the time when the direction changes
            # We'll collect all the critical times and check if the sequence is zigzag at those times
            critical_times = set()
            for i in range(1, n):
                h1, m1 = trees[i-1]
                h2, m2 = trees[i]
                # Find when the direction between i-1 and i changes
                if i % 2 == 1:
                    # Should be decreasing
                    # Find t where h1 + m1*t >= h2 + m2*t
                    # m1*t - m2*t >= h2 - h1
                    # t*(m1 - m2) >= h2 - h1
                    # If m1 > m2, then t >= (h2 - h1)/(m1 - m2)
                    if m1 > m2:
                        t = (h2 - h1) / (m1 - m2)
                        critical_times.add(t)
                    else:
                        # Never decreases, so sequence is not zigzag forever
                        return []
                else:
                    # Should be increasing
                    # Find t where h1 + m1*t <= h2 + m2*t
                    # m1*t - m2*t <= h2 - h1
                    # t*(m1 - m2) <= h2 - h1
                    # If m1 < m2, then t <= (h2 - h1)/(m1 - m2)
                    if m1 < m2:
                        t = (h2 - h1) / (m1 - m2)
                        critical_times.add(t)
                    else:
                        # Never increases, so sequence is not zigzag forever
                        return []
            # Check if the sequence is zigzag at t=0 and at all critical times
            # Also check if it's zigzag forever
            if is_zigzag():
                results.append("0 0")
            if is_forever_zigzag():
                results.append("Inf Inf")
            # Check all critical times
            for t in sorted(critical_times):
                # Check if the sequence is zigzag at time t
                # We need to compute the heights at time t
                # But since we can't compute all heights, we can check the direction changes
                # We'll check the direction between each pair of consecutive trees
                valid = True
                for i in range(1, n):
                    h1 = trees[i-1][0] + trees[i-1][1] * t
                    h2 = trees[i][0] + trees[i][1] * t
                    if i % 2 == 1:
                        if h1 >= h2:
                            valid = False
                            break
                    else:
                        if h1 <= h2:
                            valid = False
                            break
                if valid:
                    results.append(f"{int(t)} {int(t)}")
            # Also check if the sequence is zigzag forever
            if is_forever_zigzag():
                results.append("Inf Inf")
        
        # Check if the sequence is zigzag at t=0
        if is_zigzag():
            results.append("0 0")
        # Check if the sequence is zigzag forever
        if is_forever_zigzag():
            results.append("Inf Inf")
        # Check future times
        check_future()
    
    # Output the results
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()