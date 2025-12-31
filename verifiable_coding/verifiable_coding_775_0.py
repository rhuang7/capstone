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
        
        # Sort known values
        p.sort()
        
        # Check if the known values already violate the D condition
        for i in range(K):
            for j in range(i+1, K):
                if abs(p[i] - p[j]) > D:
                    results.append(-1)
                    break
            else:
                continue
            break
        else:
            # Try to find the maximum possible sum
            # We need to add (N-K) more values, all distinct, <=x, and satisfy the D condition
            # Also, the new values must be such that each has at least one other value within D
            # We can use a greedy approach: place the new values as high as possible
            # but ensuring that each new value is within D of at least one existing value
            # We can use a set to track the existing values and a list to track the new ones
            existing = set(p)
            new_values = []
            used = set()
            
            # Sort the known values
            p_sorted = sorted(p)
            
            # Try to fill the gaps
            for i in range(len(p_sorted)):
                # Find the next value that is at least p_sorted[i] + D + 1
                # and not already used
                start = p_sorted[i] + D + 1
                if start > x:
                    results.append(-1)
                    break
                # Find the first value >= start that is not used
                # We can use binary search
                low = 0
                high = len(p_sorted)
                while low < high:
                    mid = (low + high) // 2
                    if p_sorted[mid] >= start:
                        high = mid
                    else:
                        low = mid + 1
                if low < len(p_sorted):
                    # We can place a value between p_sorted[low] and p_sorted[low] - D
                    # but we need to place it as high as possible
                    # So we place it at p_sorted[low] - D
                    val = p_sorted[low] - D
                    if val not in used and val not in existing:
                        new_values.append(val)
                        used.add(val)
                        existing.add(val)
                else:
                    # No value can be placed
                    results.append(-1)
                    break
            else:
                # Check if all new values are within D of at least one existing value
                for val in new_values:
                    found = False
                    for p_val in p_sorted:
                        if abs(val - p_val) <= D:
                            found = True
                            break
                    if not found:
                        results.append(-1)
                        break
                else:
                    # Calculate the sum
                    total = sum(p) + sum(new_values)
                    results.append(total)
            continue
        
        # If we broke out of the loop, then we already added -1
        continue
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()