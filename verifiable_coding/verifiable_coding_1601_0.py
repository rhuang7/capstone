import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        P = int(data[idx+1])
        idx += 2
        
        max_score = 0
        count = 0
        
        # Precompute all possible (i, j, k) combinations
        # Since N and P are up to 1e6, brute force is not feasible
        # So we need to find the maximum score and count the valid triples efficiently
        
        # Find the maximum possible score
        # The maximum possible value of ((N mod i) mod j) mod k mod N is N-1
        # But since we are modding by N at the end, the maximum possible score is N-1
        # So we need to find if it's possible to get N-1 as the score
        
        # Try to find the maximum possible score
        max_score = 0
        for i in range(1, P+1):
            rem = N % i
            for j in range(1, P+1):
                rem2 = rem % j
                for k in range(1, P+1):
                    score = rem2 % k % N
                    if score > max_score:
                        max_score = score
        # Now count the number of triples (i, j, k) that give max_score
        
        # Reset max_score and count
        max_score = 0
        count = 0
        for i in range(1, P+1):
            rem = N % i
            for j in range(1, P+1):
                rem2 = rem % j
                for k in range(1, P+1):
                    score = rem2 % k % N
                    if score == max_score:
                        count += 1
        results.append(count)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()