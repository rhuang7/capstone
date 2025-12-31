import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for A in cases:
        balance = 0
        max_balance = 0
        for c in A:
            if c == '(':
                balance += 1
            else:
                balance -= 1
            max_balance = max(max_balance, balance)
        # Minimal length is 2 * max_balance, since each balance increase requires a corresponding decrease
        # Lexicographically smallest is all '(' followed by all ')'
        B = '(' * max_balance + ')' * max_balance
        print(B)

if __name__ == '__main__':
    solve()