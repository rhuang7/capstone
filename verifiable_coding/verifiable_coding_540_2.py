import sys
import collections

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, M = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        count = collections.Counter(A)
        required = set(range(1, M))
        missing = 0
        
        for i in range(1, M):
            if i not in count:
                missing += 1
        
        if missing > 0:
            results.append(-1)
            continue
        
        # Count how many numbers in A are less than M
        valid = 0
        for num in A:
            if num < M:
                valid += 1
        
        results.append(valid)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()