import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    results = []
    for i in range(1, T + 1):
        N = input[i]
        if len(N) == 1:
            results.append('1')
            continue
        if N[-1] in {'0', '2', '4', '6', '8'}:
            results.append('1')
        else:
            results.append('0')
    print('\n'.join(results))

if __name__ == '__main__':
    solve()