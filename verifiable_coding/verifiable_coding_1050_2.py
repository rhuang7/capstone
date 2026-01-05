import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    expressions = data[1:T+1]
    
    for s in expressions:
        balance = 0
        max_len = 0
        for i, c in enumerate(s):
            if c == '<':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                break
            max_len = i + 1
        print(max_len)

if __name__ == '__main__':
    solve()