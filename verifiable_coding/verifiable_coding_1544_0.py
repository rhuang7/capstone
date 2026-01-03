import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for K in cases:
        for i in range(1, K+1):
            if i % 2 == 1:
                print('*' * i)
            else:
                print('*' * (i//2) + ' ' * (i - i//2) + '*' * (i//2))
        print()

if __name__ == '__main__':
    solve()