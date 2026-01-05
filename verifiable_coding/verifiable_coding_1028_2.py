import sys

def solve():
    def is_armstrong(n):
        digits = list(map(int, str(n)))
        length = len(digits)
        sum_power = sum(digit ** length for digit in digits)
        return sum_power == n

    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        N = int(input[i])
        if is_armstrong(N):
            print("FEELS GOOD")
        else:
            print("FEELS BAD")

if __name__ == '__main__':
    solve()