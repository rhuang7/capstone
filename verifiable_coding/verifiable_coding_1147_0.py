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
        N = int(data[idx])
        idx += 1
        S = data[idx]
        idx += 1
        
        count = collections.Counter(S)
        odd_count = 0
        
        for char, freq in count.items():
            if freq % 2 != 0:
                odd_count += 1
        
        if odd_count > 1:
            results.append((N - (N // 2) * 2) + 1)
        else:
            results.append(N - (N // 2) * 2)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()