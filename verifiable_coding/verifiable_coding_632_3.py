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
        
        # For N > 1, the bulb is ON if the last machine is ON and has received power
        # The last machine receives power only if the previous machine is ON and has received power
        # This forms a chain: the first machine must be ON, then the second, and so on
        # The first machine is ON after 1 clap, then OFF after 2 claps, ON after 3, etc.
        # So the first machine is ON if k is odd, OFF if even
        # The second machine is ON if the first was ON and it was clapped once more
        # This continues, so the last machine is ON if the number of claps is odd and >= N
        # But for the last machine to be ON, the first N-1 machines must be ON and have received power
        # So the last machine is ON if k >= N and k is odd
        # If k < N, the last machine hasn't received power yet
        if k < N:
            print("OFF")
        else:
            if k % 2 == 1:
                print("ON")
            else:
                print("OFF")

if __name__ == '__main__':
    solve()