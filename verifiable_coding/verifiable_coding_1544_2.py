import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for K in cases:
        for i in range(1, K+1):
            for j in range(1, i+1):
                print('*', end='')
            print()
        for i in range(1, K+1):
            for j in range(1, K+1):
                if j % i == 0:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
        print()

if __name__ == '__main__':
    solve()