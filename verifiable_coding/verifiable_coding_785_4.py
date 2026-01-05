import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    A_list = list(map(int, data[1:]))
    
    results = []
    
    for A in A_list:
        D1 = 0
        max_profit = -1
        D2 = 0
        
        for D in range(1, 60):  # Since 2^59 is way larger than 1e9
            total_received = A * D
            total_given = (1 << (D - 1)) * (D) // 2  # Sum of 2^0 + 2^1 + ... + 2^(D-1) = 2^D - 1
            profit = total_received - total_given
            
            if profit > 0:
                D1 = D
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