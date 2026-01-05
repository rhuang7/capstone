import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        for i in range(k, 0, -1):
            print(str(i) * i)
        for i in range(k-1, 0, -1):
            print(str(i) * i)
        
if __name__ == '__main__':
    solve()