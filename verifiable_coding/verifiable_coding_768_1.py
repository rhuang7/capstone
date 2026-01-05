import sys
import math
from collections import defaultdict

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
        p = list(map(int, data[idx:idx + N - 1]))
        idx += N - 1
        
        # Build the tree
        tree = defaultdict(list)
        for i in range(1, N):
            tree[p[i - 1]].append(i)
        
        # Compute the maximum sum of MEX
        # The maximum sum is N * (N - 1) // 2
        # Because for each node, the MEX can be at most the size of its subtree
        # And the sum of all MEX values is maximized when each MEX is as large as possible
        # This is a known result for this problem
        results.append(N * (N - 1) // 2)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()