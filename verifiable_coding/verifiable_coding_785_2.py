import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    A_list = list(map(int, data[1:T+1]))
    
    results = []
    
    for A in A_list:
        max_d = 0
        max_profit = -1
        current_profit = 0
        day = 1
        while True:
            profit = A * day - (1 << (day - 1))
            if profit > 0:
                max_d = day
                max_profit = profit
            else:
                break
            day += 1
        
        # Find D2: the smallest D with maximum profit
        # We need to check all D up to max_d again to find the smallest D with max_profit
        max_profit = -1
        D2 = 0
        current_profit = 0
        day = 1
        while True:
            profit = A * day - (1 << (day - 1))
            if profit > max_profit:
                max_profit = profit
                D2 = day
            elif profit == max_profit:
                if D2 == 0:
                    D2 = day
            if profit <= 0:
                break
            day += 1
        
        results.append(f"{max_d} {D2}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()