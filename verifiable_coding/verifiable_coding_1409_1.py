import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        results.append(bin(N).count('1'))
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    solve()