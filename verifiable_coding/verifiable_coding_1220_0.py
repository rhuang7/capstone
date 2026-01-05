import sys
import collections

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
    
    # Preprocess: for each brand, store the prices of phones
    brand_prices = collections.defaultdict(list)
    for p, b in zip(P, B):
        brand_prices[b].append(p)
    
    results = []
    
    for _ in range(Q):
        b = int(data[idx])
        idx += 1
        K = int(data[idx])
        idx += 1
        subset = list(map(int, data[idx:idx+b]))
        idx += b
        
        # Get all prices of phones in the subset
        prices = []
        for brand in subset:
            prices.extend(brand_prices[brand])
        
        # Sort prices in descending order
        prices.sort(reverse=True)
        
        # Check if there are at least K phones
        if len(prices) < K:
            results.append("-1")
        else:
            results.append(str(prices[K-1]))
    
    print("\n".join(results))