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
            rem = N % i
            for j in range(1, P+1):
                rem2 = rem % j
                for k in range(1, P+1):
                    rem3 = rem2 % k
                    score = rem3 % N
                    if score > max_score:
                        max_score = score
                        count = 1
                    elif score == max_score:
                        count += 1
        results.append(count)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()