import sys

def solve():
    n = int(sys.stdin.buffer.read())
    if n < 10:
        print("1")
    elif 10 <= n < 100:
        print("2")
    elif 100 <= n < 1000:
        print("3")
    else:
        print("More than 3 digits")

if __name__ == '__main__':
    solve()