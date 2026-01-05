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
            # X is 000...0 (N times) => 0
            results.append(0)
            continue
        
        # Compute the length of A as a string
        len_A = len(str(A))
        
        # Compute the value of A mod M
        a_mod = A % M
        
        # Compute the value of 10^len_A mod M
        power = 1
        for _ in range(len_A):
            power = (power * 10) % M
        
        # Compute the result
        result = 0
        for _ in range(N):
            result = (result + a_mod) % M
            a_mod = (a_mod * power) % M
        
        results.append(result)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()