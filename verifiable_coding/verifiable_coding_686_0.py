import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        V1 = int(data[index+1])
        V2 = int(data[index+2])
        index += 3
        
        # Distance for stairs is sqrt(2) * N
        # Time for stairs is (sqrt(2) * N) / V1
        time_stairs = (math.sqrt(2) * N) / V1
        
        # Distance for elevator is N (goes from ground to N-th floor and then back down)
        # Time for elevator is (2 * N) / V2
        time_elevator = (2 * N) / V2
        
        if time_stairs < time_elevator:
            print("Stairs")
        else:
            print("Elevator")

if __name__ == '__main__':
    solve()