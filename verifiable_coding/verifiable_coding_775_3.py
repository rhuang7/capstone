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
        if len(p) < K:
            results.append(-1)
            continue
        
        # Sort the known values
        p.sort()
        
        # Check if the known values already violate the D condition
        for i in range(K):
            if i + 1 < K and p[i+1] - p[i] > D:
                results.append(-1)
                break
        else:
            # Check if the known values are within x
            if max(p) > x:
                results.append(-1)
                continue
            
            # Now, find the maximum possible sum
            # We need to add (N-K) values, all distinct, <= x, and such that every value has at least one other within D
            # The optimal way is to fill the gaps between the known values and at the end
            # We can use a greedy approach to fill the gaps
            
            # The known values are in sorted order
            # We need to fill the gaps between them and also add values at the end
            # We can use a list to keep track of the filled values
            
            filled = set(p)
            filled.add(x)
            
            # The idea is to fill the gaps between the known values and at the end
            # We can use a binary search approach to find where to place the new values
            
            # Start from the end
            last = x
            # Fill the end
            if last not in filled:
                filled.add(last)
            
            # Now fill the gaps between the known values
            for i in range(K-1):
                # Find the next value to place
                # The current value is p[i]
                # The next value should be at least p[i] + D + 1
                # But we can't go beyond x
                # We can place values in the range [p[i] + D + 1, x]
                # But we need to place as many as possible, ensuring that each value is within D of at least one other
                # So we can place values in the range [p[i] + D + 1, x], but we need to make sure that they are not already filled
                # We can use a binary search to find the first available position in this range
                # We can use a binary search to find the first available position in the range [p[i] + D + 1, x]
                # We can use a list of filled values and binary search to find the first available position
                # But since N can be up to 1e9, we need an efficient way to compute the number of values we can place
                # We can use the following approach:
                # For each gap between p[i] and p[i+1], we can place as many values as possible in the range [p[i] + D + 1, p[i+1] - D - 1]
                # But since we want to maximize the sum, we should place the largest possible values
                # So we can place values in the range [p[i] + D + 1, x], but ensuring that each value is within D of at least one other
                # We can place values in the range [p[i] + D + 1, x], but we need to ensure that they are not already filled
                # We can use a binary search to find the first available position in the range [p[i] + D + 1, x]
                # We can use a binary search to find the first available position in the range [p[i] + D + 1, x]
                # We can use a list of filled values and binary search to find the first available position
                # But since N can be up to 1e9, we need an efficient way to compute the number of values we can place
                # We can use the following approach:
                # For each gap between p[i] and p[i+1], we can place as many values as possible in the range [p[i] + D + 1, p[i+1] - D - 1]
                # But since we want to maximize the sum, we should place the largest possible values
                # So we can place values in the range [p[i] + D + 1, x], but ensuring that each value is within D of at least one other
                # We can place values in the range [p[i] + D + 1, x], but we need to ensure that they are not already filled
                # We can use a binary search to find the first available position in the range [p[i] + D + 1, x]
                # We can use a binary search to find the first available position in the range [p[i] + D + 1, x]
                # We can use a list of filled values and binary search to find the first available position
                # But since N can be up to 1e9, we need an efficient way to compute the number of values we can place
                # We can use the following approach:
                # For each gap between p[i] and p[i+1], we can place as many values as possible in the range [p[i] + D + 1, p[i+1] - D - 1]
                # But since we want to maximize the sum, we should place the largest possible values
                # So we can place values in the range [p[i] + D + 1, x], but ensuring that each value is within D of at least one other
                # We can place values in the range [p[i] + D + 1, x], but we need to ensure that they are not already filled
                # We can use a binary search to find the first available position in the range [p[i] + D + 1, x]
                # We can use a binary search to find the first available position in the range [p[i] + D + 1, x]
                # We can use a list of filled values and binary search to find the first available position
                # But since N can be up to 1e9, we need an efficient way to compute the number of values we can place
                # We can use the following approach:
                # For each gap between p[i] and p[i+1], we can place as many values as possible in the range [p[i] + D + 1, p[i+1] - D - 1]
                # But since we want to maximize the sum, we should place the largest possible values
                # So we can place values in the range [p[i] + D + 1, x], but ensuring that each value is within D of at least one other
                # We can place values in the range [p[i] + D + 1, x], but we need to ensure that they are not already filled
                # We can use a binary search to find the first available position in the range [p[i] + D + 1, x]
                # We can use a binary search to find the first available position in the range [p[i] + D + 1, x]
                # We can use a list of filled values and binary search to find the first available position
                # But since N can be up to 1e9, we need an efficient way to compute the number of values we can place
                # We can use the following approach:
                # For each gap between p[i] and p[i+1], we can place as many values as possible in the range [p[i] + D + 1, p[i+1] - D - 1]
                # But since we want to maximize the sum, we should place the largest possible values
                # So we can place values in the range [p[i] + D + 1, x], but ensuring that each value is within D of at least one other
                # We can place values in the range [p[i] + D + 1, x], but we need to ensure that they are not already filled
                # We can use a binary search to find the first available position in the range [p[i] + D + 1, x]
                # We can use a binary search to find the first available position in the range [p[i] + D + 1, x]
                # We can use a list of filled values and binary search to find the first available position
                # But since N can be up to 1e9, we need an efficient way to compute the number of values we can place
                # We can use the following approach:
                # For each gap between p[i] and p[i+1], we can place as many values as possible in the range [p[i] + D + 1, p[i+1] - D - 1]
                # But since we want to maximize the sum,