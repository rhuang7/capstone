import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    for N in cases:
        if int(N) % 9 == 0:
            print(0)
            continue
        digits = list(N)
        total = 0
        for i in range(len(digits)):
            digit = int(digits[i])
            if digit > 0:
                total += min(digit, 9 - digit)
        print(total)

if __name__ == '__main__':
    solve()