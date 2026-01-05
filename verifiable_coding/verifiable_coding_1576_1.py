import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for K in cases:
        for i in range(1, K+1):
            row = ''
            for j in range(1, K+1):
                row += str((i + j - 1) % K)
            print(row)
            
if __name__ == '__main__':
    solve()