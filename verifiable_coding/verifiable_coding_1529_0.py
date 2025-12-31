import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        L = list(map(int, data[idx:idx+N]))
        idx += N
        digits = L
        total = 0
        n = len(digits)
        from math import factorial
        for i in range(n):
            digit = digits[i]
            count = 0
            for d in digits:
                if d == digit:
                    count += 1
            perm = factorial(n) // factorial(count)
            place = 10 ** (n - i - 1)
            total += digit * perm * place
        results.append(str(total))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()