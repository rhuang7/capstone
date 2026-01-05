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
        
        # If we can get coal directly without any trade, we just need k trades
        if y == 1:
            results.append(k)
            continue
        
        # We need to find the optimal number of trades to get enough coal
        # We can use the trade of x sticks for 1 stick (which is a gain of x-1 sticks)
        # to maximize the number of sticks we have before converting to coal
        
        # The optimal strategy is to do as many trades as possible to get more sticks
        # before converting to coal
        # Let's find how many times we can do the first trade (stick for x sticks)
        # before we have enough sticks to convert to coal
        
        # Let's find the number of trades needed to get enough sticks to convert to coal
        # Let's assume we do 'a' trades of the first type (stick for x sticks)
        # Then we have 1 + (x-1)*a sticks
        # We need this to be >= y * (number of coals we can get)
        
        # We need to find the minimum number of trades to get at least k coals
        # Each coal requires y sticks, so we need at least k * y sticks
        # So we need 1 + (x-1)*a >= k * y
        # Solving for a: a >= (k*y - 1) / (x-1)
        
        # But we can also do some trades of the second type (y sticks for 1 coal)
        # So the total number of trades is a (first type) + b (second type)
        # where b = (1 + (x-1)*a) // y
        
        # We can binary search the number of first type trades a
        # to find the minimum total trades
        
        # Binary search for a
        low = 0
        high = 10**18
        best = 0
        while low <= high:
            mid = (low + high) // 2
            sticks = 1 + (x - 1) * mid
            coals = sticks // y
            if coals >= k:
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        
        # Now compute the total number of trades
        # best is the number of first type trades
        # coals = (1 + (x-1)*best) // y
        # total trades = best + coals
        coals = (1 + (x - 1) * best) // y
        total_trades = best + coals
        results.append(total_trades)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()