import sys
import math

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for N in cases:
        if N == 1:
            print("1 1")
            continue
        
        total = 10 ** N
        same = 0
        
        if N % 2 == 0:
            half = N // 2
            same = 10 ** half
        
        prob_p = same
        prob_q = total
        
        gcd = math.gcd(prob_p, prob_q)
        p = prob_p // gcd
        q = prob_q // gcd
        
        print(f"{p} {q}")
        
if __name__ == '__main__':
    solve()