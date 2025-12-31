import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for K in cases:
        for i in range(K):
            if i % 2 == 0:
                print('*' * (K//2 + 1))
            else:
                print('*' + ' ' * (K-2) + '*')
        print()

if __name__ == '__main__':
    solve()