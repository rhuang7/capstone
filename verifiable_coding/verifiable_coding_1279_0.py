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
            y = int(data[idx + 1])
            X.append(x)
            Y.append(y)
            idx += 2
        
        freq = collections.defaultdict(list)
        for i in range(N):
            freq[X[i]].append(Y[i])
        
        max_sum = 0
        for x1 in freq:
            for x2 in freq:
                for x3 in freq:
                    if x1 == x2 or x2 == x3 or x3 == x1:
                        continue
                    max_sum = max(max_sum, sum(freq[x1] + freq[x2] + freq[x3]))
        
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()