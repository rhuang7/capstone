import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for K in cases:
        pattern = []
        for i in range(K):
            if i % 2 == 0:
                pattern.append('0' if i == 0 else '1')
            else:
                pattern.append('1' if i == 0 else '0')
        print(''.join(pattern))
        
if __name__ == '__main__':
    solve()