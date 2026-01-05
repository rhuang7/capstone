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
        
        required = 0
        for i in range(1, M):
            if i not in count:
                required += 1
            else:
                required += min(count[i], 1)
        
        if required < M:
            results.append(-1)
        else:
            total = 0
            for i in range(1, M+1):
                if i in count:
                    total += min(count[i], 1)
            results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()