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
        
        # Convert A to a string and compute its length
        s = str(A)
        len_s = len(s)
        
        # Compute the value of A appended N times modulo M
        # We use modular exponentiation and modular arithmetic to avoid constructing the large number
        mod = 1
        for _ in range(N):
            mod = (mod * pow(10, len_s, M) + A) % M
        
        print(mod)
        
if __name__ == '__main__':
    solve()