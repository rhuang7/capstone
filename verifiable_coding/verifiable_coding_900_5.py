import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    K_list = list(map(int, data[1:]))
    
    for K in K_list:
        if K == 1:
            print(10)
            continue
        
        # For K >= 2, the number of valid road signs is 9 * 9 * 2^(K-2)
        # Explanation: Choose first digit (9 options), second digit (9 options), and the rest are determined by the symmetry
        result = (9 * 9 * pow(2, K-2, MOD)) % MOD
        print(result)

if __name__ == '__main__':
    solve()