import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    L = int(data[1])
    strings = data[2:2+N]
    
    # Sort the strings using lex order
    strings.sort()
    
    # Concatenate them
    result = ''.join(strings)
    
    print(result)

if __name__ == '__main__':
    solve()