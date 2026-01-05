import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for K in cases:
        if K == 1:
            print('*')
        else:
            for i in range(K):
                if i == 0 or i == K-1:
                    print('*' * K)
                else:
                    print('*' + ' ' * (2*(i-1)) + '*')
                    
if __name__ == '__main__':
    solve()