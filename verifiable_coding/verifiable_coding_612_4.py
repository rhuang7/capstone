import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        s = data[i]
        if '010' in s or '101' in s:
            results.append('Good')
        else:
            results.append('Bad')
    print('\n'.join(results))

if __name__ == '__main__':
    solve()