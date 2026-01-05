import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    queries = [(int(data[2*i+1]), int(data[2*i+2])) for i in range(N)]

    for i, j in queries:
        a, b = i, j
        res = 0
        while a != b:
            if a > b:
                a = a // 2
            else:
                b = b // 2
            res += 1
        print(res)

if __name__ == '__main__':
    solve()