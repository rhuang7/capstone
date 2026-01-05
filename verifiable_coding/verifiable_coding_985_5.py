import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    
    max_len = 0
    dp = {}
    
    for num in a:
        current_len = 1
        for divisor in dp:
            if num % divisor == 0:
                current_len = max(current_len, dp[divisor] + 1)
        dp[num] = current_len
        max_len = max(max_len, current_len)
    
    print(max_len)

if __name__ == '__main__':
    solve()