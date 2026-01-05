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
        # Try all combinations of digits for the i positions
        for positions in product(range(n), repeat=i):
            # Create a list of digits
            digits = list(s)
            # Change the digits at the positions
            for pos in positions:
                digits[pos] = '9'
            # Convert back to integer
            new_num = int(''.join(digits))
            # Calculate profit
            profit = new_num - S
            if profit > max_profit:
                max_profit = profit
    
    print(max_profit)

if __name__ == '__main__':
    solve()