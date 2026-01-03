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
        
        # Check if all numbers from 1 to M-1 are present
        missing = 0
        for i in range(1, M):
            if i not in freq:
                missing += 1
        
        if missing > 0:
            results.append(-1)
            continue
        
        # Count how many times M appears
        count_m = freq.get(M, 0)
        
        # The maximum number of elements we can choose is M - 1 + count_m
        max_elements = (M - 1) + count_m
        results.append(max_elements)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()