import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    
    a.sort()
    res = 0
    i = 0
    while i < n:
        res += 1
        i += 1
        while i < n and a[i] < 2 * a[i-1]:
            i += 1
    print(res)

if __name__ == '__main__':
    solve()