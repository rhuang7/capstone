import sys

def solve():
    import bisect
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    m = int(data[n+1])
    q = list(map(int, data[n+2:]))
    
    prefix = [0] * (n + 1)
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + a[i-1]
    
    for query in q:
        idx = bisect.bisect_right(prefix, query) - 1
        print(idx + 1)

if __name__ == '__main__':
    solve()