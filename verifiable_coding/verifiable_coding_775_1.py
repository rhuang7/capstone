import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        x = int(data[idx+2])
        D = int(data[idx+3])
        idx += 4
        p = list(map(int, data[idx:idx+K]))
        idx += K
        
        # Sort the known values
        p.sort()
        
        # Check if the known values already violate the D condition
        for i in range(K):
            if i + 1 < K and p[i+1] - p[i] > D:
                results.append(-1)
                break
        else:
            # We need to add (N - K) more values
            # These values must be distinct, <= x, and satisfy the D condition
            # Also, the maximum value is <= x
            # We need to maximize the sum, so we should place the new values as high as possible
            # But we have to ensure that every value has at least one other value within D
            
            # First, check if the known values can be extended to N values
            # We need to find the maximum possible values that can be added
            # The idea is to place the new values in the largest possible positions that satisfy the D condition
            
            # We can use a greedy approach to fill the gaps
            # We will use a set to keep track of used values
            used = set(p)
            used.add(x)
            
            # We need to add (N - K) values
            added = 0
            current = x
            while added < (N - K):
                # Check if current is valid
                # It must be <= x
                # It must be within D of at least one existing value
                valid = False
                for val in used:
                    if abs(current - val) <= D:
                        valid = True
                        break
                if valid:
                    used.add(current)
                    added += 1
                else:
                    # Try to decrease current by 1
                    current -= 1
                    if current < 1:
                        results.append(-1)
                        break
            else:
                # Check if all values are within D of at least one other
                # We need to ensure that for every value, there is at least one other within D
                # This is already handled by the way we added the values
                # Now calculate the sum
                total = sum(p) + sum(used) - sum(p)
                results.append(total)
        continue
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()