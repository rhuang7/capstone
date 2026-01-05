import sys

def solve():
    N = sys.stdin.buffer.read().decode().strip()
    if N == '0':
        print("1")
    else:
        digits = len(N)
        if digits == 1:
            print("1")
        elif digits == 2:
            print("2")
        elif digits == 3:
            print("3")
        else:
            print("More than 3 digits")

if __name__ == '__main__':
    solve()