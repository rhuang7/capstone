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
        # Subtract 1 to make it 0-based index
        x -= 1
        y -= 1
        # Remove the parrot at (x, y)
        a[x] -= 1
        # Parrots to the left move to x-1
        if x > 0:
            a[x - 1] += y + 1
        # Parrots to the right move to x+1
        if x < n - 1:
            a[x + 1] += (a[x] + 1) - y
    
    for num in a:
        print(num)

if __name__ == '__main__':
    solve()