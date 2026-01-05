import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for K in cases:
        for i in range(1, K+1):
            for j in range(i, K+1):
                print(j, end='')
            print()
        print()

if __name__ == '__main__':
    solve()