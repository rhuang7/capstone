import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        A = data[idx]
        idx += 1
        B = data[idx]
        idx += 1
        L = int(data[idx])
        idx += 1
        
        # Convert A and B from base 7 to decimal
        A_dec = int(A, 7)
        B_dec = int(B, 7)
        
        # Compute C = A / B (since B divides A)
        C_dec = A_dec // B_dec
        
        # Compute C modulo 7^L
        mod = 7 ** L
        C_mod = C_dec % mod
        
        # Convert C_mod from decimal to base 7
        if C_mod == 0:
            results.append('0')
        else:
            digits = []
            while C_mod > 0:
                digits.append(str(C_mod % 7))
                C_mod //= 7
            digits.reverse()
            results.append(''.join(digits))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()