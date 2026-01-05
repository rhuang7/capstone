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
        
        # We need to make k torches, each requires 1 stick and 1 coal
        # So we need k sticks and k coal
        # We start with 1 stick
        
        # First, we can use the first trade to get more sticks
        # Then, we can use the second trade to get coal
        
        # Let's find the optimal number of first trades to maximize the number of sticks
        # After that, we can use the second trade to get coal
        
        # We need to find the number of first trades (a) such that after a trades, we have enough sticks to make coal
        
        # Let's try to find the optimal a
        # After a trades, we have (x^a - 1) / (x - 1) sticks
        # We need this to be >= k (since we need k coal)
        # So we need (x^a - 1) / (x - 1) >= k
        # We can binary search a
        
        # But since x can be up to 1e9, we need to find a quickly
        
        # Let's try to find the minimal a such that (x^a - 1) / (x - 1) >= k
        # We can binary search a from 0 to 60 (since x^60 is way larger than 1e9^60)
        
        # Let's try to find a
        a = 0
        while (x ** a - 1) // (x - 1) < k:
            a += 1
        
        # Now, we have a sticks
        # We can use the second trade to get coal
        # Each trade requires y sticks, so we need to do (k // y) trades, and possibly one more if there's a remainder
        
        # But we also need to make sure we have enough sticks to make the coal
        
        # So total trades = a (first trades) + (k // y) + (1 if k % y != 0 else 0)
        
        # But we need to check if after a trades, we have enough sticks to make the coal
        # So we need to calculate how many coal we can make with the sticks we have after a trades
        
        # Let's calculate the number of sticks after a trades
        sticks = (x ** a - 1) // (x - 1)
        
        # Now, we can make (sticks // y) coal
        # So we need to make at least k coal
        # So we need to do (k // y) + (1 if k % y != 0 else 0) trades
        
        # But we also need to make sure that we have enough sticks to make the coal
        # So we need to calculate how many trades of the second type we need
        # And add that to the total
        
        # But this might not be enough, so we need to try to find the minimal number of trades
        
        # Let's try to find the minimal number of trades
        # We can try different a values and compute the total trades
        
        # Let's try to find the minimal total trades
        # We can try a from 0 to 60 and find the minimal total trades
        
        min_trades = float('inf')
        for a in range(0, 61):
            sticks = (x ** a - 1) // (x - 1)
            coal = sticks // y
            if coal >= k:
                # We can make k coal with a trades of first type and (k // y) + (1 if k % y != 0 else 0) trades of second type
                # But we need to make sure that we have enough sticks to make the coal
                # So we need to make (k // y) + (1 if k % y != 0 else 0) trades of second type
                # But we need to check if we have enough sticks for that
                # So we need to calculate how many sticks we need for that
                # Each trade of second type requires y sticks
                # So total sticks needed for coal is (k // y) * y + (k % y if k % y != 0 else 0)
                # Which is k
                # So we need to have at least k sticks
                # Which we do, since sticks >= k
                # So total trades is a + (k // y) + (1 if k % y != 0 else 0)
                total = a + (k // y) + (1 if k % y != 0 else 0)
                min_trades = min(min_trades, total)
        
        results.append(str(min_trades))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()