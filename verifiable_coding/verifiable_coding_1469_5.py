import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for K in cases:
        if K % 2 == 1:
            for i in range(K, K+K):
                print(i % 10, end='')
            print()
        else:
            for i in range(K, K+K):
                print(i % 10, end='')
            print()

if __name__ == '__main__':
    solve()