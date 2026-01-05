import sys

def solve():
    input = sys.stdin.buffer.read().decode().strip()
    N = int(input)
    if 0 <= N <= 9:
        print("1")
    elif 10 <= N <= 99:
        print("2")
    elif 100 <= N <= 999:
        print("3")
    else:
        print("More than 3 digits")

if __name__ == '__main__':
    solve()