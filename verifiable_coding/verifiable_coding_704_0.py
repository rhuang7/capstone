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
            results.append(0)
            continue
        
        # Compute the value of A modulo M
        a_mod = A % M
        
        # Compute the value of 10^k mod M for k = len(str(A))
        length = len(str(A))
        power = pow(10, length, M)
        
        # Compute the result
        result = 0
        for i in range(N):
            result = (result * power + a_mod) % M
        
        results.append(result)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()