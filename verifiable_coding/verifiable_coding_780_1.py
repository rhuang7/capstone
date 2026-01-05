import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        index += 2
        remainder = N % M
        if remainder % 2 == 0:
            results.append("EVEN")
        else:
            results.append("ODD")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()