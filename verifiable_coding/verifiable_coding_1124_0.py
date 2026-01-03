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
        N, P, Q = map(int, data[idx:idx+3])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # We need to find the maximum number of creatures that can be paid back
        # Each creature requires exactly Ai rupees, and we have P one-rupee coins and Q two-rupee coins
        # So for each creature, we need to have Ai <= P + 2*Q
        # But we also need to ensure that the coins can be distributed properly
        
        # Sort the array A
        A.sort()
        
        # We will use a greedy approach: try to pay back as many creatures as possible starting from the smallest Ai
        # We will use a two-pointer approach to find the maximum number of creatures that can be paid back
        
        # We will also use a binary search approach to find the maximum number of creatures that can be paid back
        # Let's try to find the maximum number of creatures that can be paid back using binary search
        
        # We can binary search on the number of creatures k
        # For each k, we check if it is possible to pay back the first k creatures
        
        # To check if it is possible to pay back the first k creatures:
        # We need to find the minimum number of one-rupee coins and two-rupee coins required to pay back the first k creatures
        # For each creature i (0-based), the amount is A[i]
        # We can use the fact that for each creature, we can use some number of one-rupee coins and some number of two-rupee coins
        # The total number of one-rupee coins required is sum of (A[i] - 2 * x_i), where x_i is the number of two-rupee coins used for creature i
        # The total number of two-rupee coins required is sum of x_i
        # But this is not straightforward to compute
        
        # Instead, we can use a greedy approach for each k:
        # For the first k creatures, we can try to use as many two-rupee coins as possible
        # For each creature, we can use as many two-rupee coins as possible without exceeding the amount
        # The remaining amount is paid with one-rupee coins
        # We can compute the total number of one-rupee coins and two-rupee coins needed
        
        # So for each k, we can compute the total number of one-rupee coins and two-rupee coins needed to pay back the first k creatures
        # If the total is less than or equal to P and Q, then it is possible
        
        # Let's implement this binary search approach
        
        low = 0
        high = N
        best = 0
        
        while low <= high:
            mid = (low + high) // 2
            # Check if it is possible to pay back the first mid creatures
            # We need to find the minimum number of one-rupee coins and two-rupee coins needed
            # For each creature, we can use as many two-rupee coins as possible
            # So for each creature, we can use min(A[i] // 2, Q_available) two-rupee coins
            # But since we are trying to find the minimum required, we can use the following approach:
            # For each creature, we can use as many two-rupee coins as possible, but not more than the total available
            # We can compute the total required two-rupee coins and one-rupee coins
            
            # We will use a greedy approach to compute the total required coins
            # We will try to use as many two-rupee coins as possible for each creature
            # But we need to track how many two-rupee coins are used
            # We can use a two-pointer approach to compute the required coins
            
            # Let's try to compute the required coins for the first mid creatures
            # We will use a greedy approach to use as many two-rupee coins as possible
            
            # Initialize the total two-rupee coins used and one-rupee coins used
            total_two = 0
            total_one = 0
            
            # We will iterate through the first mid creatures
            for i in range(mid):
                # For creature i, the amount is A[i]
                # We can use as many two-rupee coins as possible without exceeding the amount
                # So the maximum number of two-rupee coins we can use is min(A[i] // 2, Q - total_two)
                # But we need to use as many as possible, so we take min(A[i] // 2, Q - total_two)
                # But we need to make sure that we don't use more than the available Q
                # So we can compute the number of two-rupee coins to use
                # We can also compute the number of one-rupee coins needed
                # We can use the following approach:
                # Use as many two-rupee coins as possible, then use one-rupee coins for the remainder
                # But we need to track how many two-rupee coins are used
                # So for each creature, we can use min(A[i] // 2, Q - total_two) two-rupee coins
                # Then the remaining amount is A[i] - 2 * two_used
                # This remaining amount must be paid with one-rupee coins
                # So we need to ensure that the remaining amount is <= P - total_one
                # If not, then it is not possible to pay back this creature
                # So we can check for each creature
                
                # Let's compute the maximum number of two-rupee coins that can be used for this creature
                # We can use up to min(A[i] // 2, Q - total_two)
                # But we need to use as many as possible, so we can use the minimum of these two values
                two_used = min(A[i] // 2, Q - total_two)
                # Update the total two-rupee coins used
                total_two += two_used
                # The remaining amount is A[i] - 2 * two_used
                # This must be paid with one-rupee coins
                one_needed = A[i] - 2 * two_used
                # Check if one_needed <= P - total_one
                if one_needed > P - total_one:
                    # Not possible to pay back this creature
                    break
                total_one += one_needed
            
            # After checking all mid creatures, if we didn't break, then it is possible
            if total_two <= Q and total_one <= P:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        
        results.append(str(best))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()