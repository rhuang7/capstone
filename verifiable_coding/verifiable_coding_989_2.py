import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        X = int(data[index])
        Y = int(data[index+1])
        K = int(data[index+2])
        index += 3
        total = X + Y
        served = 0  # 0 for Chef, 1 for Paja
        # Determine how many full K-point cycles have been completed
        full_cycles = total // K
        # Determine who is serving next based on the number of full cycles
        if full_cycles % 2 == 0:
            print("Chef")
        else:
            print("Paja")

if __name__ == '__main__':
    solve()