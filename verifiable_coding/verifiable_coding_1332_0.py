import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    queries = []
    idx = 1
    for _ in range(N):
        i = int(data[idx])
        j = int(data[idx+1])
        queries.append((i, j))
        idx += 2

    for i, j in queries:
        a, b = i, j
        path = 0
        while a != b:
            if a > b:
                a = a // 2
            else:
                b = b // 2
            path += 1
        print(path)

if __name__ == '__main__':
    solve()