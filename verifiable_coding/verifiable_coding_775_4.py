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
            if i + 1 < K and p[i+1] - p[i] > D:
                results.append(-1)
                break
        else:
            # Try to fill the rest of the values
            # We need to add (N - K) values such that:
            # 1. All values are distinct and <= x
            # 2. Each value is within D of at least one other value
            # 3. The total sum is maximized
            
            # We will try to place the unknown values in the largest possible positions
            # such that they are within D of some known value
            
            # First, we need to check if the known values can be extended to N values
            # with the given constraints
            
            # We need to have at least two values in each interval of D
            # So the maximum number of values we can have is x // D * 2 + 1
            # But since we have K known values, we need to check if it's possible to add (N - K) values
            
            # Check if the known values can be extended to N values
            # The minimal number of values that can be placed is (x // D) * 2 + 1
            # But since we have K known values, we need to check if it's possible to add (N - K) values
            
            # If the number of known values is more than x // D * 2 + 1, then it's impossible
            max_vals = x // D * 2 + 1
            if K > max_vals:
                results.append(-1)
                continue
            
            # Now, we need to fill the unknown values
            # We will try to place the unknown values in the largest possible positions
            # such that they are within D of some known value
            
            # We will use a greedy approach
            # Start from the end and fill the unknown values
            
            # We need to fill (N - K) values
            # We will use a set to keep track of the values we have used
            used = set(p)
            unknowns = N - K
            
            # We will try to fill the unknowns from the end
            # Start from x and go down
            current = x
            added = 0
            while added < unknowns:
                # Find the largest value <= current that is not in used and is within D of some known value
                # We can do this by checking each known value and seeing if current - D <= p_i <= current
                found = False
                for val in p:
                    if val >= current - D and val <= current:
                        # We can place current
                        used.add(current)
                        added += 1
                        found = True
                        break
                if not found:
                    # No value can be placed, it's impossible
                    results.append(-1)
                    break
                current -= 1
            else:
                # Calculate the total sum
                total = sum(p) + sum(used - set(p))
                results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()