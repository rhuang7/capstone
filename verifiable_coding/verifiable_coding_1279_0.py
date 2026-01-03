import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        X = []
        Y = []
        for _ in range(N):
            x = int(data[idx])
            y = int(data[idx+1])
            X.append(x)
            Y.append(y)
            idx += 2
        
        count = collections.defaultdict(int)
        max_sum = 0
        
        for i in range(N):
            for j in range(i, N):
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if X[i] == X[j]:
                    continue
                if X[j] == X[i]:
                    continue
                if