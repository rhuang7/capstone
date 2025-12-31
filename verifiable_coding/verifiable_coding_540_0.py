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
        
        count = collections.defaultdict(int)
        for num in A:
            if 1 <= num <= M:
                count[num] += 1
        
        if count.get(1, 0) == 0:
            results.append(-1)
            continue
        
        required = 0
        for i in range(1, M):
            if count[i] == 0:
                required = i
                break
        if required != 0:
            results.append(-1)
            continue
        
        total = 0
        for i in range(1, M+1):
            if i in count:
                total += count[i]
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()