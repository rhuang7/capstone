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
        # We can use the coins to make up Ai, but we need to use them optimally
        
        # Sort the array A
        A.sort()
        
        # We will try to select as many as possible creatures, starting from the smallest Ai
        # We will use a greedy approach, trying to use as many two-rupee coins as possible first
        # Then use one-rupee coins for the remainder
        
        count = 0
        i = 0
        while i < N:
            ai = A[i]
            # Check if we can pay ai with the coins we have
            # We can use up to min(Q, ai // 2) two-rupee coins
            # The remaining amount is ai - 2 * two_coins
            # We need to check if we have enough one-rupee coins for the remainder
            # If yes, we can pay this creature and update the coins
            # Else, we skip this creature and move to the next
            two_coins = min(Q, ai // 2)
            one_coins_needed = ai - 2 * two_coins
            if one_coins_needed <= P:
                count += 1
                P -= one_coins_needed
                Q -= two_coins
            else:
                # Cannot pay this creature, skip it
                i += 1
            i += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()