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
        
        # Check if we can reach N and M by using ShareChat once
        # After using ShareChat once, knowledge and power are increased by 1
        # So we need to reach (N-1) and (M-1) with the remaining actions
        # Let's try all possible cases where ShareChat is used once
        # Case 1: Use ShareChat once, then solve problems and do push-ups
        # After ShareChat: knowledge = 2, power = 2
        # Need to reach N and M: (N-2) and (M-2)
        # So check if (N-2) % X == 0 and (M-2) % Y == 0
        if (N - 2) >= 0 and (M - 2) >= 0 and (N - 2) % X == 0 and (M - 2) % Y == 0:
            print("Chefirnemo")
            continue
        
        # Case 2: Use ShareChat once, then solve problems and do push-ups
        # After ShareChat: knowledge = 2, power = 2
        # Need to reach N and M: (N-2) and (M-2)
        # So check if (N-2) % X == 0 and (M-2) % Y == 0
        if (N - 2) >= 0 and (M - 2) >= 0 and (N - 2) % X == 0 and (M - 2) % Y == 0:
            print("Chefirnemo")
            continue
        
        # Case 3: Use ShareChat once, then do push-ups and solve problems
        # After ShareChat: knowledge = 2, power = 2
        # Need to reach N and M: (N-2) and (M-2)
        # So check if (N-2) % X == 0 and (M-2) % Y == 0
        if (N - 2) >= 0 and (M - 2) >= 0 and (N - 2) % X == 0 and (M - 2) % Y == 0:
            print("Chefirnemo")
            continue
        
        # If none of the cases work, print Pofik
        print("Pofik")

if __name__ == '__main__':
    solve()