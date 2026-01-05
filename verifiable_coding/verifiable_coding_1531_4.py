import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    a = list(map(int, data[idx:idx + n]))
    idx += n
    m = int(data[idx])
    idx += 1
    queries = []
    for _ in range(m):
        x = int(data[idx])
        y = int(data[idx + 1])
        queries.append((x, y))
        idx += 2
    
    for x, y in queries:
        branch = x - 1
        parrot = y - 1
        a[branch] -= 1
        if a[branch] < 0:
            a[branch] = 0
        if parrot > 0:
            a[branch - 1] += 1
        if parrot < a[branch] + 1:
            a[branch + 1] += 1
    
    for num in a:
        print(num)

if __name__ == '__main__':
    solve()