import sys

def solve():
    input = sys.stdin.buffer.read().split()
    N = int(input[0])
    L = int(input[1])
    strings = input[2:2+N]
    
    strings.sort()
    result = ''.join(strings)
    print(result)

if __name__ == '__main__':
    solve()