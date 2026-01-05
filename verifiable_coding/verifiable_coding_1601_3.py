import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    max_N = 0
    for _ in range(T):
        N = int(data[index])
        P = int(data[index+1])
        index += 2
        max_N = max(max_N, N)
    
    # Precompute for all N up to 1e6
    max_P = 10**6
    # Precompute for all N and P up to 1e6
    # We'll precompute for all N and P up to 1e6
    # But due to time constraints, we'll compute on the fly for each test case
    
    # Precompute for all N up to 1e6
    # We'll use memoization for the maximum score
    # But due to time constraints, we'll compute for each test case
    
    # For each test case
    for _ in range(T):
        N = int(data[index])
        P = int(data[index+1])
        index += 2
        
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
        
        results.append(str(count))
    
    print('\n'.join(results))