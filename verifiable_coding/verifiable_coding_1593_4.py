import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    denominations = [100, 50, 10, 5, 2, 1]
    for n in cases:
        count = 0
        for d in denominations:
            count += n // d
            n %= d
        print(count)

if __name__ == '__main__':
    solve()