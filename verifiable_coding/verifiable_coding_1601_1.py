import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        P = int(data[index+1])
        index += 2
        
        # Precompute all possible (i, j, k) combinations
        # But since N and P can be up to 1e6, we need an efficient way
        # We'll compute the maximum score M and then count the number of (i,j,k) that give M
        
        # Compute maximum score M
        M = 0
        for i in range(1, P+1):
            for j in range(1, P+1):
                for k in range(1, P+1):
                    temp = (N % i) % j % k % N
                    if temp > M:
                        M = temp
        
        # Now count the number of (i,j,k) that give M
        count = 0
        for i in range(1, P+1):
            for j in range(1, P+1):
                for k in range(1, P+1):
                    temp = (N % i) % j % k % N
                    if temp == M:
                        count += 1
        
        results.append(count)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()