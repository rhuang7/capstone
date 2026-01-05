import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    h = list(map(int, data[1:]))
    
    count = collections.defaultdict(int)
    prev = h[0]
    for i in range(1, N):
        curr = h[i]
        start = min(prev, curr)
        end = max(prev, curr)
        for height in range(start, end):
            count[height] += 1
        prev = curr
    
    max_k = 0
    for k in count.values():
        if k > max_k:
            max_k = k
    print(max_k)

if __name__ == '__main__':
    solve()