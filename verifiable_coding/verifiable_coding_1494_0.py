import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    
    a.sort()
    count = 0
    i = 0
    while i < n:
        count += 1
        j = i + 1
        while j < n and a[j] < 2 * a[i]:
            j += 1
        i = j
    print(count)

if __name__ == '__main__':
    solve()