import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        A = int(data[index])
        N = int(data[index+1])
        M = int(data[index+2])
        index += 3
        
        # Handle the case where A is 0
        if A == 0:
            print(0)
            continue
        
        # Compute the length of A as a string
        len_A = len(str(A))
        
        # Compute the value of A mod M
        a_mod = A % M
        
        # Compute the value of 10^len_A mod M
        power = pow(10, len_A, M)
        
        # Compute the result
        result = (a_mod * (pow(power, N, M) - 1) // (power - 1)) % M
        
        print(result)
        
if __name__ == '__main__':
    solve()