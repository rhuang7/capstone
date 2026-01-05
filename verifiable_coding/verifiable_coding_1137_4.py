import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    target = 20 * 100  # Annabelle's age times 100
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        prices = list(map(int, data[index:index + N]))
        index += N
        
        found = False
        price_set = set(prices)
        for price in prices:
            complement = target - price
            if complement in price_set and complement != price:
                found = True
                break
        
        print("Accepted" if found else "Rejected")

if __name__ == '__main__':
    solve()