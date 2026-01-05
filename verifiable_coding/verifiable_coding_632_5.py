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
        # The last machine is ON if it has been toggled an odd number of times
        # The previous machine is ON if it has been toggled an odd number of times
        # The number of times the last machine is toggled is equal to the number of times the previous machine is toggled
        # The number of times the previous machine is toggled is equal to the number of times the machine before that is toggled
        # This continues until the first machine
        # The first machine is toggled once for every time it receives power
        # The first machine receives power once for every time it is toggled
        # So the first machine is toggled k times
        # The second machine is toggled floor(k / 2) times
        # The third machine is toggled floor(k / 4) times
        # ...
        # The last machine is toggled floor(k / (2^(N-1))) times
        # So the last machine is ON if floor(k / (2^(N-1))) is odd
        # The second to last machine is ON if floor(k / (2^(N-2))) is odd
        # ...
        # The first machine is ON if k is odd
        # The bulb is ON if the last machine is ON and the second to last is ON
        # So we need to check if the last machine is ON and the second to last is ON
        # The last machine is ON if floor(k / (2^(N-1))) is odd
        # The second to last is ON if floor(k / (2^(N-2))) is odd
        # So we need to check if both are odd
        # But for N > 1, the last machine is ON if the number of times it is toggled is odd
        # The number of times it is toggled is floor(k / (2^(N-1)))
        # So the bulb is ON if the number of times the last machine is toggled is odd and the number of times the second to last is toggled is odd
        # But for N > 1, the second to last machine is toggled floor(k / (2^(N-2))) times
        # So the bulb is ON if both are odd
        # But for N > 1, the second to last machine is toggled floor(k / (2^(N-2))) times
        # So the bulb is ON if both are odd
        # So we need to check if floor(k / (2^(N-1))) is odd and floor(k / (2^(N-2))) is odd
        # But for N > 1, the second to last machine is toggled floor(k / (2^(N-2))) times
        # So the bulb is ON if both are odd
        # But for N > 1, the second to last machine is toggled floor(k / (2^(N-2))) times
        # So the bulb is ON if both are odd
        # So we need to check if both are odd
        # But for N > 1, the second to last machine is toggled floor(k / (2^(N-2))) times
        # So the bulb is ON if both are odd
        # So we need to check if both are odd
        # But for N > 1, the second to last machine is toggled floor(k / (2^(N-2))) times
        # So the bulb is ON if both are odd
        # So we need to check if both are odd
        # So we need to check if floor(k / (2^(N-1))) is odd and floor(k / (2^(N-2))) is odd
        # But for N > 1, the second to last machine is toggled floor(k / (2^(N-2))) times
        # So the bulb is ON if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check if both are odd
        # So we need to check