import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        # Print the uppercase letters part
        for i in range(1, k+1):
            print(chr(ord('A') + i - 1))
        # Print the numbers part
        for i in range(1, k+1):
            print(i)
        # Print a blank line after each test case except the last one
        if k != cases[-1]:
            print()

if __name__ == '__main__':
    solve()