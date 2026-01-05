import sys
import sys
from collections import defaultdict

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        tree = defaultdict(list)
        for _ in range(n-1):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            tree[u].append(v)
            tree[v].append(u)
            idx += 2
        leaves = [i for i in range(n) if len(tree[i]) == 1]
        count = 0
        while leaves:
            cnt = 0
            temp = []
            for leaf in leaves:
                if len(tree[leaf]) == 1:
                    temp.append(leaf)
            if len(temp) < k:
                break
            cnt = len(temp) // k
            count += cnt
            for i in range(cnt * k):
                leaves.remove(temp[i])
        results.append(str(count))
    print('\n'.join(results))