import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        count = bin(N).count('0') - 1  # bin(N) includes '0b' prefix, subtract 1 for '0b'
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()