import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        res = []
        for i in range(1, N+1):
            if i <= K:
                res.append(i)
            else:
                res.append(-i)
        print(' '.join(map(str, res)))

if __name__ == '__main__':
    solve()