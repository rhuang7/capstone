import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        k = int(data[index+2])
        index += 3
        
        # We need to make at least k torches, each requiring 1 stick and 1 coal
        # So we need at least k coals and k sticks
        # We can use the first trade to get more sticks, and the second to get coals
        
        # If y == 1, we can directly make k torches with k sticks (using only the first trade)
        if y == 1:
            # We need k coals, each requiring 1 stick, so we need k sticks
            # Each trade gives us x sticks for 1 stick, so we need (k - 1) trades to get k sticks
            # But we can also use the first trade to get more sticks
            # So the minimum number of trades is (k - 1) trades (each trade gives x sticks)
            # But we need to get k sticks, so we need (k - 1) trades
            # But we can also use the first trade to get more sticks
            # So the minimum number of trades is (k - 1) trades
            results.append(k - 1)
            continue
        
        # We need to find the optimal number of trades to get enough sticks and coals
        # Let's try different numbers of trades and find the minimum
        # We can use binary search or brute force, but brute force is not feasible for large k
        # So we'll use a binary search approach
        
        # The minimum number of trades is 0 (if we have enough sticks and coals)
        # The maximum number of trades is when we use only the first trade to get sticks
        # But we need to get at least k coals, so we need at least k sticks
        # So the maximum number of trades is when we use only the first trade to get sticks
        # So we can binary search between 0 and some upper bound
        
        # We'll use a binary search approach
        # We'll try to find the minimum number of trades that gives us at least k coals and k sticks
        
        # Function to check if a certain number of trades is sufficient
        def is_sufficient(trades):
            # We can use some of the trades for the first trade (stick to stick)
            # And the rest for the second trade (stick to coal)
            # Let's say we use 'a' trades for the first trade, and 'b' trades for the second trade
            # a + b = trades
            # After a trades, we have (1 * x^a) sticks
            # After b trades, we have (1 * x^a - b * y) sticks
            # We need to have at least k coals and k sticks
            # So we need (1 * x^a - b * y) >= k and b >= k
            # But this is complicated, so we'll try to find the optimal a and b
            
            # We can use the first trade to get as many sticks as possible
            # So we can try to use as many first trades as possible
            # Then use the second trade to get coals
            # Let's try to find the optimal number of first trades
            # Let's try all possible numbers of first trades from 0 to some upper bound
            # For each possible a, we can compute the number of second trades needed
            # And check if the total trades is <= the given trades
            # We can try to find the optimal a for the given trades
            
            # Try all possible a from 0 to some upper bound
            # The upper bound can be log(x, k) + 1
            # But since x can be up to 1e9, we can try up to 60
            # Because 2^60 is way bigger than 1e9
            # So we'll try a from 0 to 60
            for a in range(0, 61):
                # After a trades, we have x^a sticks
                # Then we can use (trades - a) trades for the second trade
                # Each second trade uses y sticks, so we need (trades - a) * y sticks
                # We need to have x^a - (trades - a) * y >= k
                # And (trades - a) >= k
                # So we need to find if there exists an a such that:
                # x^a >= (trades - a) * y + k
                # And (trades - a) >= k
                # So we can try to find if there exists an a that satisfies these conditions
                # Let's compute the required number of second trades
                # Let's compute the number of second trades needed to get k coals
                # We need (trades - a) >= k
                # So trades - a >= k
                # a <= trades - k
                # So a can be from 0 to min(trades - k, 60)
                if a > trades - k:
                    continue
                # Now, after a trades, we have x^a sticks
                # We need to have x^a - (trades - a) * y >= k
                # Let's compute the required number of sticks
                required_sticks = (trades - a) * y + k
                if x ** a >= required_sticks:
                    return True
            return False
        
        # Binary search for the minimum number of trades
        low = 0
        high = 2 * 10**9  # A safe upper bound
        answer = high
        
        while low <= high:
            mid = (low + high) // 2
            if is_sufficient(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        results.append(answer)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()