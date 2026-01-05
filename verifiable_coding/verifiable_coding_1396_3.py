import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        X = int(data[index+2])
        Y = int(data[index+3])
        index += 4
        
        # Initial values
        knowledge = 1
        power = 1
        
        # Check if we can reach N and M without using ShareChat
        if (N - 1) % X == 0 and (M - 1) % Y == 0:
            print("Chefirnemo")
            continue
        
        # Check if we can reach N and M with ShareChat once
        # After using ShareChat once, knowledge and power are increased by 1
        # So we need to check if (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or (N - 1 - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (N - 1) % X == 0 and (M - 1 - 1) % Y == 0
        # Or (