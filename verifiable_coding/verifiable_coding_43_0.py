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
        b = list(map(int, data[idx:idx + n]))
        idx += n
        
        # For each dish, choose the minimum between a_i and b_i
        # But we need to consider that some dishes are picked up by courier and others by Petya
        # The total time is the maximum of (time for courier dishes) and (sum of time for Petya dishes)
        # So we need to select which dishes to use courier for to minimize this maximum
        
        # We can try all possible combinations, but that's too slow
        # Instead, we can try to choose the best dishes for courier and the rest for Petya
        
        # We can try to select the top k dishes to use courier for, and the rest for Petya
        # We can try all possible k from 0 to n and find the minimum maximum time
        
        min_time = float('inf')
        # Try all possible k (number of dishes to use courier for)
        for k in range(n + 1):
            # Select the k dishes with the smallest a_i - b_i (since we want to choose courier for dishes where a_i is better than b_i)
            # Sort the dishes based on a_i - b_i
            # We can precompute this for each test case
            # But for efficiency, we can do it on the fly
            # For each dish, compute a_i - b_i
            # Then select the top k dishes with the smallest (a_i - b_i)
            # Wait, no: we want to choose courier for dishes where a_i is better than b_i
            # So for each dish, if a_i < b_i, we should choose courier for it
            # Otherwise, we should choose Petya to pick it up
            # So we can precompute for each dish whether a_i < b_i
            # Then, for the dishes where a_i < b_i, we can choose to use courier or not
            # But this is not straightforward
            # Another approach: for each dish, we can choose to use courier or not
            # The total time is the maximum of (max courier time) and (sum of Petya times)
            # So we can try all possible subsets, but that's too slow
            # So we need an efficient way to find the best subset
            
            # We can try to select the top k dishes to use courier for, where a_i is better than b_i
            # So for each dish, compute a_i - b_i
            # Then sort the dishes by a_i - b_i
            # Then for each k, select the top k dishes with the smallest a_i - b_i (i.e., where a_i is better than b_i)
            # Then, the courier time is the maximum of the a_i of those k dishes
            # The Petya time is the sum of b_i of the remaining dishes
            # The total time is the maximum of these two values
            
            # So we can sort the dishes by a_i - b_i
            # Then for each k, select the first k dishes (those with the smallest a_i - b_i)
            # Then compute the max a_i of those k dishes and the sum b_i of the rest
            # And take the maximum of those two values
            # Then find the minimum of all these values for all k
            
            # So let's proceed with this approach
            
            # Compute a_i - b_i for all dishes
            diff = [a[i] - b[i] for i in range(n)]
            
            # Sort the dishes by diff
            sorted_dishes = sorted(zip(diff, a, b), key=lambda x: x[0])
            
            # Now, for each k from 0 to n, select the first k dishes (those with the smallest diff)
            # For each k, the courier time is the max a_i of those k dishes
            # The Petya time is the sum of b_i of the remaining (n - k) dishes
            # The total time is the maximum of these two values
            # We need to find the minimum of these values over all k
            
            # Precompute prefix sums of b_i
            prefix_b = [0] * (n + 1)
            for i in range(n):
                prefix_b[i + 1] = prefix_b[i] + sorted_dishes[i][2]
            
            # Precompute max a_i for the first k dishes
            max_a = [0] * (n + 1)
            for i in range(n):
                max_a[i + 1] = max(max_a[i], sorted_dishes[i][1])
            
            # Now, for each k, compute the total time
            for k in range(n + 1):
                courier_time = max_a[k]
                petya_time = prefix_b[n] - prefix_b[k]
                total_time = max(courier_time, petya_time)
                if total_time < min_time:
                    min_time = total_time
        
        results.append(str(min_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()