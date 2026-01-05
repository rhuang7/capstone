import sys

def solve():
    data = sys.stdin.buffer.read().split()
    for s in data:
        if len(s) < 1:
            print("Invalid")
            continue
        if len(set(s)) != len(s):
            print("Invalid")
        else:
            print("Valid")
            return

if __name__ == '__main__':
    solve()