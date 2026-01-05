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
        s = list(N)
        total = 0
        for i in range(len(s)):
            digit = int(s[i])
            if digit > 0:
                total += (9 - digit) if (9 - digit) < (digit) else digit
        print(total)

if __name__ == '__main__':
    solve()