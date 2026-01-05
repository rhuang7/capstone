import sys
import math

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    
    N = int(data[idx]); idx +=1
    K = int(data[idx]); idx +=1
    Q = int(data[idx]); idx +=1
    
    a = int(data[idx]); idx +=1
    b = int(data[idx]); idx +=1
    c = int(data[idx]); idx +=1
    d = int(data[idx]); idx +=1
    e = int(data[idx]); idx +=1
    f = int(data[idx]); idx +=1
    r = int(data[idx]); idx +=1
    s = int(data[idx]); idx +=1
    t = int(data[idx]); idx +=1
    m = int(data[idx]); idx +=1
    A1 = int(data[idx]); idx +=1
    
    L1 = int(data[idx]); idx +=1
    La = int(data[idx]); idx +=1
    Lc = int(data[idx]); idx +=1
    Lm = int(data[idx]); idx +=1
    D1 = int(data[idx]); idx +=1
    Da = int(data[idx]); idx +=1
    Dc = int(data[idx]); idx +=1
    Dm = int(data[idx]); idx +=1
    
    A = [0] * (N + 1)
    A[1] = A1
    
    for x in range(2, N + 1):
        t_pow_x = pow(t, x)
        if (t_pow_x % s) <= r:
            A[x] = (a * A[x-1] * A[x-1] + b * A[x-1] + c) % m
        else:
            A[x] = (d * A[x-1] * A[x-1] + e * A[x-1] + f) % m
    
    sum_qualities = 0
    product_qualities = 1
    mod = 10**9 + 7
    
    for _ in range(Q):
        L1 = (La * L1 + Lc) % Lm
        D1 = (Da * D1 + Dc) % Dm
        L = L1 + 1
        R = min(L + K - 1 + D1, N)
        
        min_val = A[L]
        for i in range(L + 1, R + 1):
            if A[i] < min_val:
                min_val = A[i]
        
        sum_qualities += min_val
        product_qualities = (product_qualities * min_val) % mod
    
    print(sum_qualities, product_qualities)

if __name__ == '__main__':
    main()