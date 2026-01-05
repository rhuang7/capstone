import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        for i in range(k):
            if i % 2 == 0:
                print('*' * (k - i - 1) + str(k - i))
            else:
                print('*' * (k - i - 1) + str(k - i))
        print()

if __name__ == '__main__':
    solve()