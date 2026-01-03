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
        # So we need to reach N-1 and M-1 with the remaining actions
        # Let's check if it's possible
        # After using ShareChat, knowledge = 1 + 1 = 2, power = 1 + 1 = 2
        # So we need to reach N-1 and M-1 from 2
        # So we need (N-1 - 2) % X == 0 and (M-1 - 2) % Y == 0
        if (N - 2) % X == 0 and (M - 2) % Y == 0:
            results.append("Chefirnemo")
            continue
        
        # If none of the above, it's impossible
        results.append("Pofik")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()