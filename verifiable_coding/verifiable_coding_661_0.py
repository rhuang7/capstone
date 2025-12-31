import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    X_list = list(map(int, data[1:T+1]))
    N_list = list(map(int, data[T+1:]))
    
    for i in range(T):
        N = N_list[i]
        X = X_list[i]
        
        if N == 0:
            print("yes")
            continue
        
        S = int(math.isqrt(N))
        diff = N - S * S
        
        if diff <= 0.01 * X * N:
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    solve()