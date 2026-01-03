import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        if (N * M) % 2 == 0:
            results.append("Yes")
        else:
            results.append("No")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()