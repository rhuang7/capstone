import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    
    P = list(map(int, data[idx:idx+N]))
    idx += N
    B = list(map(int, data[idx:idx+N]))
    idx += N
    
    # Preprocess: for each brand, store the sorted list of prices in descending order
    brand_prices = {i: [] for i in range(1, 7)}
    for price, brand in zip(P, B):
        brand_prices[brand].append(price)
    
    # Sort each brand's prices in descending order
    for brand in brand_prices:
        brand_prices[brand].sort(reverse=True)
    
    output = []
    
    for _ in range(Q):
        b = int(data[idx])
        idx += 1
        K = int(data[idx])
        idx += 1
        subset = list(map(int, data[idx:idx+b]))
        idx += b
        
        # Collect all prices of the preferred brands
        prices = []
        for brand in subset:
            prices.extend(brand_prices[brand])
        
        # Sort the collected prices in descending order
        prices.sort(reverse=True)
        
        # Check if there are at least K phones
        if len(prices) < K:
            output.append("-1")
        else:
            # Find the K-th costliest phone
            output.append(str(prices[K-1]))
    
    print('\n'.join(output))