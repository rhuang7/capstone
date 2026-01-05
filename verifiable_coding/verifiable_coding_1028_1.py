import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        N = int(data[i])
        digits = list(map(int, str(N)))
        length = len(digits)
        sum_power = sum(digit ** length for digit in digits)
        if sum_power == N:
            print("FEELS GOOD")
        else:
            print("FEELS BAD")

if __name__ == '__main__':
    solve()