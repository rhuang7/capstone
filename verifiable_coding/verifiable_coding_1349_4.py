import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = data[i]
        sum_digits = sum(int(d) for d in N)
        if sum_digits % 3 == 0:
            results.append('1')
        else:
            results.append('0')
    print('\n'.join(results))

if __name__ == '__main__':
    solve()