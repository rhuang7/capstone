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
        # After using ShareChat, knowledge and power increase by 1
        # So we need to reach (N-1, M-1) with the remaining actions
        # So we need to check if (N-1 - 1) % X == 0 and (M-1 - 1) % Y == 0
        if (N - 2) % X == 0 and (M - 2) % Y == 0:
            results.append("Chefirnemo")
            continue
        
        # Check if we can reach N and M with some combination of actions
        # We need to find non-negative integers a, b, c such that:
        # knowledge = 1 + a*X + c
        # power = 1 + b*Y + c
        # where c is 0 or 1 (ShareChat used once)
        
        # Case 1: c = 0
        # knowledge = 1 + a*X
        # power = 1 + b*Y
        # Need to solve for a and b such that 1 + a*X = N and 1 + b*Y = M
        # Which is same as before
        
        # Case 2: c = 1
        # knowledge = 1 + a*X + 1 = 2 + a*X
        # power = 1 + b*Y + 1 = 2 + b*Y
        # Need to solve for a and b such that 2 + a*X = N and 2 + b*Y = M
        
        # Check if N and M are at least 2
        if N < 2 or M < 2:
            results.append("Pofik")
            continue
        
        # Check if we can reach N and M with ShareChat
        if (N - 2) % X == 0 and (M - 2) % Y == 0:
            results.append("Chefirnemo")
            continue
        
        # Check if we can reach N and M without ShareChat
        if (N - 1) % X == 0 and (M - 1) % Y == 0:
            results.append("Chefirnemo")
            continue
        
        # If none of the above, it's impossible
        results.append("Pofik")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()