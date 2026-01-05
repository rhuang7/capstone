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
        
        # Compute max_score
        for i in range(1, P+1):
            temp = N % i
            for j in range(1, P+1):
                temp2 = temp % j
                for k in range(1, P+1):
                    temp3 = temp2 % k
                    current_score = temp3 % N
                    if current_score > max_score:
                        max_score = current_score
                        count = 1
                    elif current_score == max_score:
                        count += 1
        results.append(count)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()