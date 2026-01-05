import sys
import math

def solve():
    import sys
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
                    final = mod_k % N
                    if final > max_score:
                        max_score = final
                        count = 1
                    elif final == max_score:
                        count += 1
        
        results.append(count)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()