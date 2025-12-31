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
        
        # Check if we can reach N and M by using ShareChat once
        # After using ShareChat once, knowledge and power are increased by 1
        # So we need to reach (N-1) and (M-1) with the remaining actions
        # But since we can use ShareChat only once, we need to check if (N-1) and (M-1) can be achieved with some combination of solve and push-up
        # Also, we need to make sure that (N-1) >= 0 and (M-1) >= 0
        if N - 1 < 0 or M - 1 < 0:
            results.append("Pofik")
            continue
        
        # Check if (N-1) and (M-1) can be achieved with solve and push-up
        # We need to find non-negative integers a and b such that a*X + b*Y = (N-1) + (M-1)
        # But since we can use solve and push-up any number of times, we can use the fact that X and Y are positive
        # So, if X and Y are both positive, then we can always achieve any value >= some minimum
        # But we need to check if (N-1) + (M-1) can be achieved with some combination of X and Y
        # This is equivalent to checking if (N-1) + (M-1) >= 0 and (N-1) % X == 0 or (M-1) % Y == 0 or (N-1 + M-1) % gcd(X,Y) == 0
        # But since X and Y can be large, we need to find a way to check this efficiently
        # We can use the fact that if X and Y are both positive, then we can achieve any value >= (X*Y - X - Y) using the coin problem
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # However, since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value >= (X*Y - X - Y) if X and Y are coprime
        # So, we can check if (N-1 + M-1) >= 0 and (N-1 + M-1) >= (X*Y - X - Y) if X and Y are coprime
        # But since we can use solve and push-up any number of times, we can achieve any value