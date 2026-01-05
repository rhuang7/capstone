import sys

def solve():
    data = sys.stdin.buffer.read().decode().split()
    for s in data:
        if len(s) < 1:
            print("Invalid")
            continue
        if len(set(s)) != len(s):
            print("Invalid")
        else:
            print("Valid")
            break

if __name__ == '__main__':
    solve()