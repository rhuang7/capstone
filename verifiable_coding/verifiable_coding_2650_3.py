import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    L = int(data[1])
    S = data[2:2+N]
    
    S.sort()
    result = ''.join(S)
    print(result)

if __name__ == '__main__':
    solve()