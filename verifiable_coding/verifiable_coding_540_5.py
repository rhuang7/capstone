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
        
        freq = collections.defaultdict(int)
        for num in A:
            if 1 <= num <= M:
                freq[num] += 1
        
        count = 0
        for i in range(1, M+1):
            if i in freq:
                count += 1
            else:
                break
        else:
            # Check if all numbers from 1 to M-1 are present
            if M - 1 in freq:
                count += 1
            else:
                count = 0
        
        if count == M:
            results.append(count)
        else:
            results.append(-1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()