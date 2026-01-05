import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for K in cases:
        row = 1
        current = 1
        for i in range(K):
            if i % 2 == 0:
                print(''.join(str(current) for _ in range(row)), end='')
                current += row
                row = 1
            else:
                print(' ' + ''.join(str(current) for _ in range(row)), end='')
                current += row
                row = 1
            if i != K-1:
                print()
        print()

if __name__ == '__main__':
    solve()