import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    A_list = list(map(int, data[1:]))

    results = []

    for A in A_list:
        max_d = 0
        max_profit = -1
        current_profit = 0
        d = 0
        while True:
            d += 1
            profit = A * d - (1 << (d - 1))
            if profit > 0:
                max_d = d
                max_profit = profit
            else:
                break
        # Now find D2: the D with maximum profit
        # We need to check all D up to max_d
        # But since we already have the max_d, we can check from 1 to max_d
        # But we can optimize by checking from 1 to max_d and track the max profit
        # However, since we already have the max_d, we can check from 1 to max_d
        # and find the smallest D with maximum profit
        # But for efficiency, we can track it during the loop
        # So we need to redo the loop and track the max profit and the smallest D
        max_profit = -1
        d2 = 0
        current_profit = 0
        d = 0
        while True:
            d += 1
            profit = A * d - (1 << (d - 1))
            if profit > 0:
                if profit > max_profit:
                    max_profit = profit
                    d2 = d
                elif profit == max_profit:
                    if d2 == 0 or d < d2:
                        d2 = d
            else:
                break
        results.append(f"{max_d} {d2}")

    print("\n".join(results))

if __name__ == '__main__':
    solve()