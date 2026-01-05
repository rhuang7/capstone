import sys

def solve():
    input = sys.stdin.buffer.read().split()
    N = int(input[0])
    L = int(input[1])
    strings = input[2:2+N]
    
    # Sort the strings using lex order
    strings.sort()
    
    # Concatenate them
    result = ''.join(strings)
    
    print(result)

if __name__ == '__main__':
    solve()