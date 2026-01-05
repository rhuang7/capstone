import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        N = int(data[i])
        last_digit = N % 10
        first_digit = N
        while first_digit >= 10:
            first_digit //= 10
        print(first_digit + last_digit)

if __name__ == '__main__':
    solve()