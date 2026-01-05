import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    Xs = list(map(int, data[1:T+1]))
    
    for X in Xs:
        if X == 2:
            print(2)
        else:
            print(X & (X - 1) + 1)

if __name__ == '__main__':
    solve()