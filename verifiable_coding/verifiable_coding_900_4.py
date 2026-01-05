import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    K_list = list(map(int, data[1:T+1]))
    
    for K in K_list:
        if K == 1:
            print(10)
            continue
        
        # For K >= 2, the number of valid road signs is 9 * 9 * 2^(K-2)
        # Explanation:
        # - Choose the first digit (9 options: 1-9)
        # - Choose the second digit (9 options: 0-9 excluding the first)
        # - The remaining K-2 digits can be either of the two chosen digits
        # - Each such choice gives two valid road signs (since the other side is determined)
        result = (9 * 9) % MOD
        for _ in range(K-2):
            result = (result * 2) % MOD
        print(result)

if __name__ == '__main__':
    solve()