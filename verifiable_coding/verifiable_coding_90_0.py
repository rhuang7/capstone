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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        l = list(map(int, data[idx:idx+n]))
        idx += n
        
        locked = [i for i in range(n) if l[i] == 1]
        unlocked = [i for i in range(n) if l[i] == 0]
        unlocked_values = [a[i] for i in unlocked]
        
        # We want to minimize k, which is the maximum j where prefix sum is negative
        # To minimize k, we want to make the prefix sums as positive as possible early on
        # So we sort the unlocked values in a way that makes the prefix sums as positive as possible
        # We can try different sorting strategies and choose the one that gives the minimal k
        
        # Try different sorting strategies
        # Strategy 1: Sort unlocked values in ascending order
        sorted_asc = sorted(unlocked_values)
        # Strategy 2: Sort unlocked values in descending order
        sorted_desc = sorted(unlocked_values, reverse=True)
        # Strategy 3: Sort unlocked values with smallest negative first, then positives
        # This is a heuristic to try to make prefix sums positive as early as possible
        sorted_neg_then_pos = sorted(unlocked_values, key=lambda x: (x < 0, x))
        
        # Try each strategy and find the one with minimal k
        best_k = n + 1
        best_arr = a.copy()
        
        for sorted_vals in [sorted_asc, sorted_desc, sorted_neg_then_pos]:
            new_a = a.copy()
            for i, pos in enumerate(unlocked):
                new_a[pos] = sorted_vals[i]
            
            # Compute prefix sums
            prefix_sums = []
            current_sum = 0
            for val in new_a:
                current_sum += val
                prefix_sums.append(current_sum)
            
            # Find k
            k = 0
            for j in range(n):
                if prefix_sums[j] < 0:
                    k = j + 1
                else:
                    break  # Once a non-negative prefix sum is found, no need to check further
            
            if k < best_k:
                best_k = k
                best_arr = new_a
        
        # Output the best_arr
        results.append(' '.join(map(str, best_arr)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()