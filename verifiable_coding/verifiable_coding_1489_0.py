import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    S = int(input[0])
    K = int(input[1])

    s = str(S)
    n = len(s)

    # Generate all possible numbers by changing up to K digits
    from itertools import product

    max_profit = 0

    # Try changing 0 to K digits
    for i in range(K + 1):
        # Generate all combinations of digits for the i digits to change
        for positions in product(range(n), repeat=i):
            # Create a new number by changing the digits at positions
            new_s = list(s)
            for pos in positions:
                new_s[pos] = '9'  # Change to maximum possible digit
            new_num = int(''.join(new_s))
            profit = new_num - S
            if profit > max_profit:
                max_profit = profit

    print(max_profit)

if __name__ == '__main__':
    solve()