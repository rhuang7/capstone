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
        # We can use the coins to make up Ai, but we need to use as many as possible
        
        # Sort the array A
        A.sort()
        
        # We will use a greedy approach
        # We will try to use as many two-rupee coins as possible first, then one-rupee coins
        # But we need to find the optimal way to use the coins
        
        # We will use a two-pointer approach
        # One pointer for the start of the array (i), and one for the end (j)
        # We will try to find the maximum number of creatures that can be paid back
        
        # Initialize variables
        i = 0
        j = N - 1
        count = 0
        
        while i <= j:
            # Try to use the current creature (A[i])
            # We need to check if we can pay A[i] with the coins we have
            # We can use as many two-rupee coins as possible, then one-rupee coins
            # So we can compute how many two-rupee coins are needed for A[i]
            # And then check if we have enough coins
            
            # We can use the two-rupee coins first
            # Let's try to use as many two-rupee coins as possible for A[i]
            # The number of two-rupee coins needed is (A[i] // 2)
            # But we can't use more than Q two-rupee coins
            # So the maximum number of two-rupee coins we can use is min(Q, A[i] // 2)
            # Then the remaining amount is A[i] - (number of two-rupee coins used * 2)
            # Which must be covered by one-rupee coins
            # So the number of one-rupee coins needed is (A[i] - (number of two-rupee coins used * 2))
            # Which must be <= P
            
            # We can try to use as many two-rupee coins as possible
            # But we can also try to use as few as possible to save coins for other creatures
            # So we need to find the optimal way to use the coins
            
            # Let's try to use as many two-rupee coins as possible for A[i]
            # But we can't use more than Q two-rupee coins
            # So the maximum number of two-rupee coins we can use is min(Q, A[i] // 2)
            # Let's try that
            two_coins = min(Q, A[i] // 2)
            one_coins = A[i] - two_coins * 2
            if one_coins <= P:
                count += 1
                P -= one_coins
                Q -= two_coins
                i += 1
            else:
                # We can't pay this creature, so we try to pay the next one
                # But we need to find the optimal way to use the coins
                # So we can try to use as few two-rupee coins as possible
                # So we can try to use 0 two-rupee coins
                one_coins = A[i]
                if one_coins <= P:
                    count += 1
                    P -= one_coins
                    i += 1
                else:
                    # We can't pay this creature either
                    # So we try to pay the next one
                    j -= 1
        
        results.append(str(count))
    
    print('\n'.join(results))