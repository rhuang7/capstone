import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    S = int(data[0])
    K = int(data[1])

    s = str(S)
    n = len(s)
    max_profit = 0

    for i in range(n):
        if K == 0:
            break
        # Try to change the i-th digit to 9
        new_num = s[:i] + '9' * (n - i)
        new_num = int(new_num)
        profit = new_num - S
        if profit > max_profit:
            max_profit = profit
        K -= 1

    print(max_profit)

if __name__ == '__main__':
    solve()