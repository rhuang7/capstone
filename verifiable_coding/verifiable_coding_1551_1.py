import sys

def solve():
    input = sys.stdin.buffer.read().split(b'\n')
    T = int(input[0])
    for i in range(1, T+1):
        S = input[i].decode().strip()
        if ' not ' in S:
            print("Real Fancy")
        else:
            print("regularly fancy")

if __name__ == '__main__':
    solve()