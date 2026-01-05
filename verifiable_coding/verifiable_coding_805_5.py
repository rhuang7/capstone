import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        max_profit = 0
        for _ in range(N):
            S_i = int(data[idx])
            P_i = int(data[idx+1])
            V_i = int(data[idx+2])
            idx += 3
            # Current number of stores for this type
            current_stores = S_i
            # People who want to buy this type
            people = P_i
            # People who will buy from Chef
            people_per_store = people // (current_stores + 1)
            if people % (current_stores + 1) != 0:
                people_per_store = people // (current_stores + 1)
            # Profit for Chef
            profit = people_per_store * V_i
            if profit > max_profit:
                max_profit = profit
        results.append(str(max_profit))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()