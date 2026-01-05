import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    S = int(data[0])
    K = int(data[1])
    
    s = str(S)
    n = len(s)
    
    # Generate all possible numbers by changing up to K digits
    from itertools import product
    
    max_profit = 0
    for i in range(n):
        for digits in product(range(10), repeat=K):
            # Change the first K digits starting from position i
            new_s = list(s)
            for j in range(K):
                new_s[i + j] = str(digits[j])
            new_num = int(''.join(new_s))
            profit = new_num - S
            if profit > max_profit:
                max_profit = profit
    print(max_profit)

if __name__ == '__main__':
    solve()