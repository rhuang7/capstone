import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
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
            results.append("Chefirnemo")
            continue
        
        # Try using ShareChat once
        # After using ShareChat, knowledge and power are increased by 1
        # So we need to reach (N-1, M-1) with the remaining actions
        # Knowledge after ShareChat: 2 + a*X
        # Power after ShareChat: 2 + b*Y
        # So we need 2 + a*X = N and 2 + b*Y = M
        # Which means a*X = N - 2 and b*Y = M - 2
        # So check if (N - 2) is non-negative and divisible by X, and (M - 2) is non-negative and divisible by Y
        if (N - 2) >= 0 and (M - 2) >= 0 and (N - 2) % X == 0 and (M - 2) % Y == 0:
            results.append("Chefirnemo")
            continue
        
        # Check if we can reach N and M with ShareChat and some other actions
        # After ShareChat, knowledge is 2 + a*X and power is 2 + b*Y
        # So we need 2 + a*X = N and 2 + b*Y = M
        # Which means a*X = N - 2 and b*Y = M - 2
        # So check if (N - 2) is non-negative and divisible by X, and (M - 2) is non-negative and divisible by Y
        # But we already did that, so now check if we can reach N and M with some combination of actions
        # Also check if we can reach N and M with some combination of actions without ShareChat
        # If not, then it's impossible
        # But we already checked that
        # So now check if we can reach N and M with some combination of actions
        # If not, then it's impossible
        # So check if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 2) >= 0 and (M - 2) >= 0 and (N - 2) % X == 0 and (M - 2) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X == 0 and (M - 1) % Y == 0
        # Or if (N - 1) >= 0 and (M - 1) >= 0 and (N - 1) % X