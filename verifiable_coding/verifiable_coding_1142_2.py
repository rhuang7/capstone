import sys

def solve():
    import bisect
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    wealth = list(map(int, input[1:n+1]))
    ranks = []
    sorted_wealth = []
    for w in wealth:
        idx = bisect.bisect_left(sorted_wealth, w)
        ranks.append(idx + 1)
        bisect.insort(sorted_wealth, w)
    for r in ranks:
        print(r)

if __name__ == '__main__':
    solve()