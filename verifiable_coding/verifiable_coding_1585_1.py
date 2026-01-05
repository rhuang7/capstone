import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        A = int(input[idx])
        B = int(input[idx+1])
        idx += 2
        min_val = A + B
        max_val = A + B
        if A < B:
            min_val = B
        else:
            min_val = A
        print(f"{min_val} {max_val}")

if __name__ == '__main__':
    solve()