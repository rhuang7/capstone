import sys

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
    
    from collections import defaultdict
    brand_dict = defaultdict(list)
    for p, b in zip(P, B):
        brand_dict[b].append(p)
    
    results = []
    
    for _ in range(Q):
        b = int(data[idx])
        idx += 1
        K = int(data[idx])
        idx += 1
        subset = list(map(int, data[idx:idx+b]))
        idx += b
        
        prices = []
        for brand in subset:
            prices.extend(brand_dict[brand])
        
        if not prices:
            results.append("-1")
            continue
        
        prices.sort(reverse=True)
        if K > len(prices):
            results.append("-1")
        else:
            results.append(str(prices[K-1]))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()