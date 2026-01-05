import sys

def solve():
    import bisect
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    m = int(data[n+1])
    queries = list(map(int, data[n+2:]))
    
    prefix = []
    total = 0
    for num in a:
        total += num
        prefix.append(total)
    
    for q in queries:
        idx = bisect.bisect_right(prefix, q) - 1
        print(idx + 1)

if __name__ == '__main__':
    solve()