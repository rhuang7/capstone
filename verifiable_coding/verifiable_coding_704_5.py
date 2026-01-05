import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        A = int(data[index])
        N = int(data[index+1])
        M = int(data[index+2])
        index += 3
        
        # Handle the case where A is 0
        if A == 0:
            # X is 0 repeated N times, so X mod M is 0
            results.append(0)
            continue
        
        # Convert A to a string and compute its length
        s = str(A)
        len_s = len(s)
        
        # Compute the value of A repeated N times mod M
        # We can use modular arithmetic to avoid constructing the large number
        # The idea is to compute the contribution of each repetition of A
        # and accumulate it modulo M
        
        # Compute the value of A mod M
        a_mod = A % M
        
        # Compute the value of 10^len_s mod M
        power = pow(10, len_s, M)
        
        # Initialize the result
        result = 0
        
        # Compute the contribution of each repetition
        for _ in range(N):
            result = (result * power + a_mod) % M
        
        results.append(result)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()