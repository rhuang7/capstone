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
        
        required = 1
        for i in range(1, M):
            if count.get(i, 0) == 0:
                results.append(-1)
                break
            required += 1
        
        if required == M:
            total = 0
            for i in range(1, M+1):
                total += count[i]
            results.append(total)
        else:
            results.append(-1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()