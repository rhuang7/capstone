import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        missing_positions = [i for i in range(n) if a[i] == -1]
        m = 0
        possible_k = 0
        
        # For each pair of consecutive missing positions, calculate the possible k range
        for i in range(len(missing_positions) - 1):
            left = missing_positions[i]
            right = missing_positions[i + 1]
            
            # Get the values at the left and right of the missing positions
            left_val = a[left - 1] if left > 0 else a[left + 1]
            right_val = a[right + 1] if right < n - 1 else a[right - 1]
            
            # The k must be between left_val and right_val to minimize the max difference
            low = min(left_val, right_val)
            high = max(left_val, right_val)
            
            # Update the possible k range
            m = max(m, high - low)
            possible_k = max(possible_k, high)
        
        # The minimal possible m is the maximum of all the ranges
        # We can choose k as the maximum of the high values to minimize the max difference
        results.append(f"{m} {possible_k}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()