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
        
        # For N > 1, the bulb is ON if the last machine is ON and the power is flowing through it
        # The power flows through the chain of machines only if the first machine is ON and the power is on
        # The first machine toggles every time it is clapped, but only when it is receiving power
        # The first machine receives power when it is ON and the power source is on
        # The power source is on when the first machine is ON and it has been clapped an odd number of times
        
        # The first machine is ON when k is odd
        # The power source is on when the first machine is ON
        # So the power flows through the chain if the first machine is ON (k is odd)
        
        # The last machine is ON if it has been toggled an odd number of times
        # The number of times the last machine is toggled is equal to the number of times the first machine is ON
        # Which is equal to the number of times the first machine is clapped and is ON, which is floor((k + 1) / 2)
        
        # So the last machine is ON if floor((k + 1) / 2) is odd
        
        toggle_count = (k + 1) // 2
        if toggle_count % 2 == 1:
            print("ON")
        else:
            print("OFF")

if __name__ == '__main__':
    solve()