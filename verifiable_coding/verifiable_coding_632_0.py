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
        
        # For N > 1, the bulb is ON if the last machine is ON and the previous one is ON
        # The last machine is ON if it was toggled an odd number of times
        # The previous machine is ON if it was toggled an odd number of times and received power
        # The previous machine receives power if the machine before it was ON
        # This is a chain of toggles, where each machine is toggled once for each time it receives power
        # The first machine is toggled once for each clap
        # The second machine is toggled once for each time the first machine is ON
        # The third machine is toggled once for each time the second machine is ON
        # And so on
        
        # The number of times the i-th machine is toggled is equal to the number of times the (i-1)-th machine is ON
        # The i-th machine is ON if it was toggled an odd number of times
        
        # The first machine is toggled k times
        # The second machine is toggled floor(k / 2) times
        # The third machine is toggled floor(k / 4) times
        # The fourth machine is toggled floor(k / 8) times
        # ...
        # The i-th machine is toggled floor(k / (2^(i-1))) times
        
        # The last machine is ON if it was toggled an odd number of times
        # The last machine is toggled floor(k / (2^(N-1))) times
        # So, if floor(k / (2^(N-1))) is odd, the bulb is ON, else OFF
        
        power = k
        for i in range(1, N):
            power = power // 2
        if power % 2 == 1:
            print("ON")
        else:
            print("OFF")

if __name__ == '__main__':
    solve()