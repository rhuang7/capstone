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
        
        # Try using ShareChat once
        # After using ShareChat, knowledge and power are increased by 1
        # So we need to reach (N-1, M-1) with the remaining actions
        # So we need to check if (N-1 - 1) % X == 0 and (M-1 - 1) % Y == 0
        if (N - 2) % X == 0 and (M - 2) % Y == 0:
            print("Chefirnemo")
            continue
        
        # Check if it's possible to reach N and M with some combination
        # After using ShareChat, we can use solve and do push-up
        # So we need to check if (N - 1 - a) % X == 0 and (M - 1 - b) % Y == 0
        # Where a + b = 1 (since ShareChat is used once)
        # So we check for a = 0, b = 1 and a = 1, b = 0
        # Also check if (N - 1) % X == 0 and (M - 1) % Y == 0 (without ShareChat)
        # And if (N - 2) % X == 0 and (M - 2) % Y == 0 (with ShareChat)
        # If none of these are true, then it's impossible
        # Also check if (N - 1) >= 1 and (M - 1) >= 1 (since we can't have negative values)
        # Also check if (N - 2) >= 0 and (M - 2) >= 0 (since we can't have negative values)
        # Also check if X and Y are positive
        if X == 0 or Y == 0:
            print("Pofik")
            continue
        
        if (N - 1) >= 1 and (M - 1) >= 1 and (N - 1) % X == 0 and (M - 1) % Y == 0:
            print("Chefirnemo")
            continue
        
        if (N - 2) >= 0 and (M - 2) >= 0 and (N - 2) % X == 0 and (M - 2) % Y == 0:
            print("Chefirnemo")
            continue
        
        print("Pofik")

if __name__ == '__main__':
    solve()