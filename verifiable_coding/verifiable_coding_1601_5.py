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
        
        max_score = 0
        count = 0
        
        for i in range(1, P+1):
            mod_i = N % i
            for j in range(1, P+1):
                mod_j = mod_i % j
                for k in range(1, P+1):
                    mod_k = mod_j % k
                    score = mod_k % N
                    if score > max_score:
                        max_score = score
                        count = 1
                    elif score == max_score:
                        count += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()