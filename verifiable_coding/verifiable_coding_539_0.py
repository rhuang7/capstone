import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        # Since M = N + 1, and Bob starts at a corner and moves along the perimeter
        # The perimeter is 4 * N, but since he starts at a corner, the effective perimeter is 2 * (N - 1)
        # The minimum number of moves is (M // (2 * (N - 1))) if M % (2 * (N - 1)) == 0 else (M // (2 * (N - 1))) + 1
        perimeter = 2 * (N - 1)
        M = N + 1
        if M % perimeter == 0:
            res = M // perimeter
        else:
            res = (M // perimeter) + 1
        results.append(res)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()