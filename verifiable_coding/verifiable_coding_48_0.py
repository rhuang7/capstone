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
        
        # To craft k torches, we need k sticks and k coal
        # We can use the first trade to gain more sticks, then use the second trade to get coal
        # We need to find the optimal number of trades to get at least k coal
        
        # If y == 1, we can get coal for 1 stick, so we just need k trades
        if y == 1:
            results.append(k)
            continue
        
        # If x == 2, we can trade 1 stick for 2 sticks, which is a net gain of 1 stick
        # So we can use this to get more sticks, then trade for coal
        # We need to find how many times we can trade to get enough sticks to get k coal
        
        # Let's find the minimum number of trades to get at least k coal
        # We can do this by trying different numbers of trades for the first type
        # and see how many we need for the second type
        
        # We can try to find the optimal number of trades for the first type
        # Let's try up to 2 * k trades for the first type
        # Because after that, we can just trade for coal directly
        
        min_trades = float('inf')
        for i in range(0, 2 * k + 1):
            # After i trades of the first type, we have (1 + (x - 1) * i) sticks
            # Then we can trade for coal: (1 + (x - 1) * i) // y
            # The number of trades for the second type is (1 + (x - 1) * i) // y
            # But we need at least k coal, so we need (1 + (x - 1) * i) // y >= k
            # So we need (1 + (x - 1) * i) >= k * y
            # Solving for i: i >= (k * y - 1) / (x - 1)
            # So we can try i = max(0, (k * y - 1) // (x - 1))
            # But we can also try a few values around that to find the minimum
            # So we'll try i from max(0, (k * y - 1) // (x - 1) - 100) to (k * y - 1) // (x - 1) + 100
            # and find the minimum trades
            
            # But to avoid too many iterations, we can just try a few values
            # and find the minimum
            # We can try i from 0 to 2 * k, but that's too slow for large k
            # So we'll try a few values around the optimal i
            
            # Let's try i = max(0, (k * y - 1) // (x - 1) - 100) to (k * y - 1) // (x - 1) + 100
            # and find the minimum trades
            
            # But for the sake of time, we'll try a few values
            # Let's try i = 0, 1, 2, ..., up to 2 * k
            # and find the minimum trades
            # But for large k, this is too slow
            # So we'll find the optimal i using binary search
            
            # Let's find the minimum i such that (1 + (x - 1) * i) >= k * y
            # i >= (k * y - 1) / (x - 1)
            # So the minimum i is ceil((k * y - 1) / (x - 1))
            # So we can try i = ceil((k * y - 1) / (x - 1))
            # and also try i = ceil((k * y - 1) / (x - 1)) - 1 and +1 to find the minimum
            # Then compute the number of trades for the second type
            # and find the minimum total trades
            
            # Let's compute the optimal i
            # i = max(0, (k * y - 1 + (x - 1 - 1)) // (x - 1))
            # i = max(0, (k * y - 1 + x - 2) // (x - 1))
            i = max(0, (k * y - 1 + x - 2) // (x - 1))
            
            # Try i, i-1, i+1
            for j in range(max(0, i - 100), min(2 * k, i + 100) + 1):
                # After j trades of the first type, we have (1 + (x - 1) * j) sticks
                # Then we can trade for coal: (1 + (x - 1) * j) // y
                # We need at least k coal
                # So we need (1 + (x - 1) * j) // y >= k
                # So we need (1 + (x - 1) * j) >= k * y
                # So j >= (k * y - 1) / (x - 1)
                # So we can compute the number of trades for the second type
                # which is (1 + (x - 1) * j) // y
                # But we need to get at least k coal
                # So we need to compute the number of trades for the second type
                # which is ceil((1 + (x - 1) * j) / y)
                # But we can just compute it as (1 + (x - 1) * j) // y
                # and if it is less than k, we need to add more trades
                # So we can compute the number of trades for the second type
                # as (1 + (x - 1) * j) // y
                # and if it is less than k, we need to add (k - (1 + (x - 1) * j) // y) trades
                # So the total number of trades is j + max(0, k - (1 + (x - 1) * j) // y)
                # We need to find the minimum total trades
                sticks = 1 + (x - 1) * j
                coal = sticks // y
                if coal >= k:
                    total = j + (coal - k)
                    min_trades = min(min_trades, total)
                else:
                    # We need to trade more for coal
                    # So we need to add (k - coal) trades
                    total = j + (k - coal)
                    min_trades = min(min_trades, total)
        
        results.append(min_trades)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()