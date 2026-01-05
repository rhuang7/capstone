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
        # - Choose the second digit (9 options: 0-9 except first)
        # - The remaining K-2 digits can be either of the two digits (2 options each)
        # - Each pair of digits (a, b) and (b, a) are considered distinct
        ans = 9 * 9 * (2 ** (K - 2)) % MOD
        print(ans)

if __name__ == '__main__':
    solve()