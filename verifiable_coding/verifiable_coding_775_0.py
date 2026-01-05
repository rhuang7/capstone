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
        
        # Check if the known values already violate constraints
        if len(p) != K:
            results.append(-1)
            continue
        
        # Sort known values
        p.sort()
        
        # Check if any two known values are more than D apart
        for i in range(K-1):
            if p[i+1] - p[i] > D:
                results.append(-1)
                break
        else:
            # Try to fill in the missing values
            # We need to add (N - K) values such that:
            # 1. All values are distinct and <= x
            # 2. Every value has at least one other value within D
            # 3. The total sum is maximized
            
            # We can use a greedy approach to fill in the missing values
            # by placing them as high as possible while maintaining the constraints
            
            # We'll use a set to keep track of used values
            used = set(p)
            
            # We'll use a list to keep track of the current values
            current = p.copy()
            
            # We'll use a list to keep track of the current values in sorted order
            current.sort()
            
            # We'll use a list to keep track of the current values in sorted order
            # and insert new values in the right position
            # We'll also keep track of the maximum value
            max_val = current[-1]
            
            # We need to add (N - K) values
            for _ in range(N - K):
                # Try to place the next value as high as possible
                # while maintaining the constraints
                # We'll try to place it at the end of the current list
                # and check if it's within D of the previous value
                # If not, we'll try to place it in the middle
                
                # Try to place it at the end
                candidate = max_val + 1
                if candidate > x:
                    # Not possible, try to place it in the middle
                    # Find the position where it can be placed
                    pos = bisect.bisect_right(current, max_val - D)
                    if pos == 0:
                        # Can't place it anywhere
                        results.append(-1)
                        break
                    # Place it at pos
                    candidate = current[pos] - D
                    if candidate <= current[pos] and candidate >= current[pos-1]:
                        # Place it at pos
                        current.insert(pos, candidate)
                        used.add(candidate)
                        max_val = candidate
                    else:
                        # Not possible
                        results.append(-1)
                        break
                else:
                    # Place it at the end
                    current.append(candidate)
                    used.add(candidate)
                    max_val = candidate
            
            else:
                # Check if all values are within D of at least one other value
                # We can do this by checking if the maximum value is within D of the minimum value
                # If not, then there's at least one value that is not within D of any other value
                if max_val - min(current) > D:
                    results.append(-1)
                else:
                    # Calculate the sum
                    total = sum(current)
                    results.append(total)
            continue
        
        results.append(-1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()