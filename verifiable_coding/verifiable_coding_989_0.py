import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        X = int(input[idx])
        Y = int(input[idx+1])
        K = int(input[idx+2])
        idx += 3
        total = X + Y
        served = 0
        # Determine how many full K-point cycles have occurred
        full_cycles = total // K
        # After each full cycle, the server changes
        if full_cycles % 2 == 0:
            print("Chef")
        else:
            print("Paja")

if __name__ == '__main__':
    solve()