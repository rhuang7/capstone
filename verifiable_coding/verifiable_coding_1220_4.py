import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    Q = int(data[idx+1])
    idx += 2
    
    P = list(map(int, data[idx:idx+N]))
    idx += N
    
    B = list(map(int, data[idx:idx+N]))
    idx += N
    
    # Preprocess: for each brand, store the prices of phones of that brand
    brand_prices = {i: [] for i in range(1, 7)}
    for p, b in zip(P, B):
        brand_prices[b].append(p)
    
    results = []
    
    for _ in range(Q):
        b = int(data[idx])
        K = int(data[idx+1])
        idx += 2
        
        preference = list(map(int, data[idx:idx+b]))
        idx += b
        
        # Collect all prices of phones in the preference subset
        prices = []
        for brand in preference:
            prices.extend(brand_prices[brand])
        
        # Sort the prices in descending order
        prices.sort(reverse=True)
        
        # Check if there are at least K phones
        if len(prices) < K:
            results.append("-1")
        else:
            results.append(str(prices[K-1]))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()