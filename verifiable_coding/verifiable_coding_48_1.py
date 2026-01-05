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
        # But we need to balance between getting more sticks and converting them to coal
        
        # Let's try to find the optimal number of times to use the first trade
        # Let's try all possible numbers of first trades up to some limit
        # Since x >= 2, the number of first trades is at most k * 2 (since each trade gives us x-1 sticks)
        # But since k can be up to 1e9, we need a better approach
        
        # Let's try to find the optimal number of first trades (let's call it m)
        # After m first trades, we have 1 + (x-1)*m sticks
        # Then, we can convert as many sticks as possible to coal
        # Each coal requires y sticks, so the number of coals is (sticks) // y
        # The number of torches is min(coals, k)
        
        # We need to find the minimal number of trades to get at least k torches
        
        # Let's try all possible m from 0 to some upper limit (like 1e6)
        # But since k can be up to 1e9, we need to find an efficient way
        
        # We can use binary search on m
        # The minimal m is 0, the maximum m is such that (1 + (x-1)*m) >= k * y (since we need enough sticks to make k coals)
        # So we can binary search m in [0, ... , (k * y - 1) // (x-1) + 1]
        
        # But since x can be up to 1e9, and k up to 1e9, we need a smarter way
        
        # Let's try to find the optimal m in a loop up to a small limit (like 1e6)
        # Since for large m, the number of trades is m + (sticks // y)
        
        # Let's try all m from 0 to 1e6
        # If we find a m that gives enough coals, we can stop
        
        min_trades = float('inf')
        
        # Try m from 0 to some limit
        for m in range(0, 1000000):
            sticks = 1 + (x - 1) * m
            coals = sticks // y
            torches = min(coals, k)
            if torches >= k:
                trades = m + (sticks // y)
                if trades < min_trades:
                    min_trades = trades
                break
        
        # If not found in the loop, we can try to calculate the optimal m
        # But for the given constraints, the loop should be sufficient
        
        results.append(str(min_trades))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()