import sys

def solve():
    input = sys.stdin.buffer.read().split(b'\n')
    T = int(input[0])
    cases = input[1:T+1]
    for s in cases:
        s = s.decode().strip()
        if ' not ' in s:
            print("Real Fancy")
        else:
            print("regularly fancy")

if __name__ == '__main__':
    solve()