import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for s in cases:
        balance = 0
        max_len = 0
        for i, char in enumerate(s):
            if char == '<':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                break
            max_len = i + 1
        print(max_len)

if __name__ == '__main__':
    solve()