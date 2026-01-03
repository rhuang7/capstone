import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        for i in range(k, 0, -1):
            print(''.join(str(j) for j in range(i, 0, -1)))
        for i in range(k-1, 0, -1):
            print(''.join(str(j) for j in range(i, 0, -1)))

if __name__ == '__main__':
    solve()