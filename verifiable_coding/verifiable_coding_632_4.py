import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N = int(input[idx])
        k = int(input[idx+1])
        idx += 2
        if N == 1:
            if k % 2 == 1:
                print("ON")
            else:
                print("OFF")
            continue
        # For N > 1, the bulb is lit if the last machine is ON and receives power
        # The last machine receives power if the (N-1)th machine is ON and receives power
        # This continues until the first machine, which receives power if the power source is on
        # The power source is on if the first machine is ON and receives power
        # The first machine is ON if it is clapped an odd number of times
        # The first machine receives power if it is clapped at least once
        # So the bulb is ON if k >= 1 and k is odd
        if k >= 1 and k % 2 == 1:
            print("ON")
        else:
            print("OFF")

if __name__ == '__main__':
    solve()