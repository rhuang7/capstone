import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = input[0]
    quotes = input[1:]
    for s in quotes:
        if ' not ' in s:
            print("Real Fancy")
        else:
            print("regularly fancy")

if __name__ == '__main__':
    solve()