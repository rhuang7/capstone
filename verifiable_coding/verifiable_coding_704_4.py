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
        
        # Convert A to a string
        s = str(A)
        len_s = len(s)
        
        # Compute the modulo of the number formed by appending A N times
        # X = A * (10^(len_s * (N-1)) + 10^(len_s * (N-2)) + ... + 10^0)
        # We can compute this using modular exponentiation and geometric series
        mod = M
        power = 1
        total = 0
        
        for i in range(N):
            total = (total * power + A) % mod
            power = (power * pow(10, len_s, mod)) % mod
        
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()