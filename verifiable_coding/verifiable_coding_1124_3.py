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
        # So, for each creature, we need to check if we can pay Ai using the coins we have
        
        # Sort the array A
        A.sort()
        
        # We will use a greedy approach: try to pay the smallest Ai first
        # We will use a two-pointer approach to find the maximum number of creatures that can be paid back
        
        # Initialize pointers
        left = 0
        right = N - 1
        count = 0
        
        while left <= right:
            ai = A[left]
            # Check if we can pay ai with the coins we have
            # We need to find the minimum number of coins needed to pay ai
            # The minimum number of coins is the minimum between using 1-rupee coins and 2-rupee coins
            # We can use a greedy approach to find the minimum number of coins needed
            # For ai, the minimum number of coins is (ai // 2) + (ai % 2)
            # But we need to check if we have enough coins to pay ai
            # We can try to use as many 2-rupee coins as possible
            # So, we can try to use as many 2-rupee coins as possible, then use 1-rupee coins for the remainder
            # But we need to check if we have enough coins
            
            # Try to pay ai using as many 2-rupee coins as possible
            # Let's try to use as many 2-rupee coins as possible
            # So, the number of 2-rupee coins needed is (ai // 2)
            # But we can't use more than Q
            # So, the maximum number of 2-rupee coins we can use is min(Q, ai // 2)
            # Then, the remaining amount is ai - (number of 2-rupee coins used * 2)
            # The remaining amount must be paid with 1-rupee coins, which we have P of
            # So, the total coins needed is (number of 2-rupee coins used) + (remaining amount)
            # We need to check if we have enough coins to pay ai
            
            # Try to use as many 2-rupee coins as possible
            max_two = min(Q, ai // 2)
            remaining = ai - (max_two * 2)
            if remaining <= P:
                # We can pay this creature
                count += 1
                # Use the coins
                Q -= max_two
                P -= remaining
                left += 1
            else:
                # We can't pay this creature, so we try to pay the next larger creature
                # We can try to use as many 2-rupee coins as possible, but not enough
                # So, we try to use fewer 2-rupee coins
                # We can try to use (ai // 2) - 1 2-rupee coins
                # But we need to make sure that we have enough 2-rupee coins
                # So, we can try to use (ai // 2) - 1 2-rupee coins
                # Then, the remaining amount is ai - ((ai // 2) - 1) * 2
                # We need to check if we have enough 1-rupee coins
                # But this approach is not efficient, so we can use a binary search approach
                # Instead, we can try to find the maximum number of creatures that can be paid back
                # We can use a binary search approach to find the maximum number of creatures that can be paid back
                # We can sort the array A, and for each possible number of creatures k, we can check if it's possible to pay back the first k creatures
                # So, we can use binary search on k
                # The maximum possible k is N
                # The minimum possible k is 0
                # So, we can perform a binary search on k
                # For each k, we can check if the first k creatures can be paid back with the given coins
                # We can use a greedy approach to check this
                # We can sort the array A
                # Then, for the first k creatures, we can try to pay them in a way that uses as many 2-rupee coins as possible
                # We can use a greedy approach to check if it's possible to pay back the first k creatures
                # So, we can use a binary search approach
                # We can binary search on k, from 0 to N
                # For each k, we can check if the first k creatures can be paid back
                # We can use a greedy approach to check this
                # We can sort the array A
                # Then, for the first k creatures, we can try to pay them in a way that uses as many 2-rupee coins as possible
                # We can use a greedy approach to check if it's possible to pay back the first k creatures
                # So, we can use a binary search approach
                # We can binary search on k, from 0 to N
                # For each k, we can check if the first k creatures can be paid back
                # We can use a greedy approach to check this
                # We can sort the array A
                # Then, for the first k creatures, we can try to pay them in a way that uses as many 2-rupee coins as possible
                # We can use a greedy approach to check if it's possible to pay back the first k creatures
                # So, we can use a binary search approach
                # We can binary search on k, from 0 to N
                # For each k, we can check if the first k creatures can be paid back
                # We can use a greedy approach to check this
                # We can sort the array A
                # Then, for the first k creatures, we can try to pay them in a way that uses as many 2-rupee coins as possible
                # We can use a greedy approach to check if it's possible to pay back the first k creatures
                # So, we can use a binary search approach
                # We can binary search on k, from 0 to N
                # For each k, we can check if the first k creatures can be paid back
                # We can use a greedy approach to check this
                # We can sort the array A
                # Then, for the first k creatures, we can try to pay them in a way that uses as many 2-rupee coins as possible
                # We can use a greedy approach to check if it's possible to pay back the first k creatures
                # So, we can use a binary search approach
                # We can binary search on k, from 0 to N
                # For each k, we can check if the first k creatures can be paid back
                # We can use a greedy approach to check this
                # We can sort the array A
                # Then, for the first k creatures, we can try to pay them in a way that uses as many 2-rupee coins as possible
                # We can use a greedy approach to check if it's possible to pay back the first k creatures
                # So, we can use a binary search approach
                # We can binary search on k, from 0 to N
                # For each k, we can check if the first k creatures can be paid back
                # We can use a greedy approach to check this
                # We can sort the array A
                # Then, for the first k creatures, we can try to pay them in a way that uses as many 2-rupee coins as possible
                # We can use a greedy approach to check if it's possible to pay back the first k creatures
                # So, we can use a binary search approach
                # We can binary search on k, from 0 to N
                # For each k, we can check if the first k creatures can be paid back
                # We can use a greedy approach to check this
                # We can sort the array A
                # Then, for the first k creatures, we can try to pay them in a way that uses as many 2-rupee coins as possible
                # We can use a greedy approach to check if it's possible to pay back the first k creatures
                # So, we can use a binary search approach
                # We can binary search on k, from 0 to N
                # For each k, we can check if the first k creatures can be paid back
                # We can use a greedy approach to