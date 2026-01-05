import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        N = int(data[i])
        sum_digits = sum(int(d) for d in str(N))
        print(sum_digits)

if __name__ == '__main__':
    solve()