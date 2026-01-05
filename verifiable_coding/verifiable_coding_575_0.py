import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        n = len(s)
        P = 1
        prev = 1
        for i in range(n):
            if s[i] == '<':
                if prev == 1:
                    P = 2
                else:
                    P += 1
                prev = P
            elif s[i] == '>':
                if prev == 1:
                    P = 2
                else:
                    P += 1
                prev = P
            else:  # '='
                if prev == 1:
                    P = 2
                else:
                    P += 1
                prev = P
        print(P)

if __name__ == '__main__':
    solve()