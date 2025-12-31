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
            people_per_store = P_i // (S_i + 1)
            profit = people_per_store * V_i
            if profit > max_profit:
                max_profit = profit
        results.append(str(max_profit))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()