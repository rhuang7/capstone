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
        
        # For each dish, we can choose either a_i or b_i
        # We need to choose the minimum of a_i and b_i for each dish
        # But we also need to consider that if we choose a_i, then the courier will take a_i time
        # If we choose b_i, then Petya will take b_i time
        # The total time is the maximum of all chosen times
        
        # We can choose to take a_i or b_i for each dish
        # To minimize the total time, we need to choose the minimum of a_i and b_i for each dish
        # But we also need to consider that if we choose a_i for some dishes, then the couriers will take a_i time
        # and Petya will have to go to the restaurants where he didn't choose delivery
        # So the total time is the maximum of:
        # - the maximum a_i for dishes where we choose delivery
        # - the sum of b_i for dishes where we choose to go personally
        
        # We can try all possible subsets of dishes to choose delivery for, but that's too slow
        # Instead, we can try to find the optimal choice by trying different numbers of dishes to choose delivery for
        
        # We can try all possible k from 0 to n, and for each k, try to choose k dishes to use delivery and the rest to go personally
        # For each k, we can choose the k dishes with the smallest (a_i - b_i) to use delivery, and the rest to go personally
        # This is because for a dish, if a_i < b_i, it's better to use delivery, otherwise it's better to go personally
        
        # We can precompute the difference between a_i and b_i for each dish
        # Then, we can sort the dishes based on this difference
        
        # For each k, we can choose the k dishes with the smallest (a_i - b_i) to use delivery
        # The total time is the maximum of:
        # - the maximum a_i among the k dishes chosen for delivery
        # - the sum of b_i among the (n - k) dishes not chosen for delivery
        
        # We can precompute the sorted list of (a_i - b_i) and the prefix sums of b_i
        # Then, for each k, we can try to choose the k dishes with the smallest (a_i - b_i)
        
        # Precompute the list of (a_i - b_i) and the list of b_i
        diff = [a[i] - b[i] for i in range(n)]
        b_list = b
        
        # Sort the dishes based on diff
        sorted_dishes = sorted(zip(diff, b_list), key=lambda x: x[0])
        
        # Precompute the prefix sums of b_list
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + sorted_dishes[i][1]
        
        # Try all possible k from 0 to n
        min_time = float('inf')
        for k in range(n + 1):
            # Choose k dishes to use delivery
            # The first k dishes in the sorted list are the ones with the smallest (a_i - b_i)
            # So we take their a_i and the rest are b_i
            # The maximum time is the max between the max a_i of the first k dishes and the sum of b_i of the rest
            # But we need to calculate the max a_i of the first k dishes
            # We can precompute the max a_i for the first k dishes
            # So we precompute the max a_i for the first k dishes
            # But since we have sorted the dishes by (a_i - b_i), we can't directly get the max a_i
            # So we need to precompute the max a_i for the first k dishes
            # But since we have sorted the dishes by (a_i - b_i), we can't directly get the max a_i
            # So we need to precompute the max a_i for the first k dishes
            
            # So we need to precompute the max a_i for the first k dishes
            # So we can precompute a list of max_a for the first k dishes
            # But since we have sorted the dishes by (a_i - b_i), we can't directly get the max a_i
            # So we need to precompute the max a_i for the first k dishes
            # So we can precompute a list of max_a for the first k dishes
            # So we can precompute a list of max_a for the first k dishes
            # We can do this by iterating through the sorted dishes and keeping track of the maximum a_i
            max_a = 0
            for i in range(k):
                max_a = max(max_a, sorted_dishes[i][0] + sorted_dishes[i][1])
            # The sum of b_i for the remaining (n - k) dishes
            sum_b = prefix_sum[n] - prefix_sum[k]
            # The total time is the maximum between max_a and sum_b
            total_time = max(max_a, sum_b)
            min_time = min(min_time, total_time)
        
        results.append(str(min_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()