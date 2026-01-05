import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N = int(input[idx])
        V1 = int(input[idx+1])
        V2 = int(input[idx+2])
        idx += 3
        
        # Distance for stairs is sqrt(2)*N
        time_stairs = (math.sqrt(2) * N) / V1
        
        # Distance for elevator is N (goes from ground to N-th floor, then back down)
        time_elevator = (N / V2) * 2
        
        if time_stairs < time_elevator:
            print("Stairs")
        else:
            print("Elevator")

if __name__ == '__main__':
    solve()