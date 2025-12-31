import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    prices = list(map(int, data[2:2+n]))
    
    prices.sort()
    count = 0
    total = 0
    for price in prices:
        if total + price <= k:
            total += price
            count += 1
        else:
            break
    print(count)

if __name__ == '__main__':
    solve()