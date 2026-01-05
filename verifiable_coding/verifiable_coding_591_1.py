import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    for N in cases:
        n = int(N)
        if n == 1:
            print(10)
        else:
            # The nth smallest number with digit sum divisible by 10 and > 0
            # The nth number is n * 10 + 7
            print(n * 10 + 7)

if __name__ == '__main__':
    solve()