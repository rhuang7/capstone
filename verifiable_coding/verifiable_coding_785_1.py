import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    A_list = list(map(int, data[1:]))
    
    results = []
    
    for A in A_list:
        # Find D1: maximum D where profit is positive
        # Profit = A*D - sum(2^i for i in 0..D-1) = A*D - (2^D - 1)
        # We want A*D - (2^D - 1) > 0
        # So find max D where A*D > 2^D - 1
        D1 = 0
        while True:
            try:
                D = D1 + 1
                if A * D > (1 << D) - 1:
                    D1 = D
                else:
                    break
            except:
                break
        
        # Find D2: maximum profit, smallest D if tie
        max_profit = -1
        D2 = 0
        for D in range(1, 60):  # since 2^60 is way larger than 1e9
            profit = A * D - (1 << D) + 1
            if profit > max_profit:
                max_profit = profit
                D2 = D
            elif profit == max_profit:
                if D < D2:
                    D2 = D
        
        results.append(f"{D1} {D2}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()