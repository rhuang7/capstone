import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for K in cases:
        for i in range(K):
            row = ''
            for j in range(K):
                if j == i:
                    row += str(j)
                else:
                    row += str(j)
            print(row)
        for i in range(K-1, -1, -1):
            row = ''
            for j in range(K):
                if j == i:
                    row += str(j)
                else:
                    row += str(j)
            print(row)

if __name__ == '__main__':
    solve()