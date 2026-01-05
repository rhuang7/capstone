import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        if N == 1:
            results.append('1')
        else:
            if N % 2 == 1:
                results.append(str(6 * (N // 2) + 1))
            else:
                results.append(str(6 * (N // 2) + 6))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()