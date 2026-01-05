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
        # After using ShareChat, knowledge and power increase by 1
        # So we need to reach (N-1, M-1) with the remaining actions
        # We can use solve and push-up to reach (N-1, M-1)
        # So we need to check if (N-1 - 1) % X == 0 and (M-1 - 1) % Y == 0
        if (N - 2) % X == 0 and (M - 2) % Y == 0:
            print("Chefirnemo")
            continue
        
        # Check if it's possible to reach N and M with some combination of actions
        # We can use solve and push-up to reach (N - 1, M - 1)
        # So we need to check if (N - 1) % X == 0 and (M - 1) % Y == 0
        if (N - 1) % X == 0 and (M - 1) % Y == 0:
            print("Chefirnemo")
            continue
        
        # If none of the above, it's impossible
        print("Pofik")

if __name__ == '__main__':
    solve()