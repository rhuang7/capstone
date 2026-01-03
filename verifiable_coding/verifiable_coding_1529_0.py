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
            count = 1
            for j in range(i):
                if digits[j] == digit:
                    count += 1
            perm = factorial(n) // factorial(count)
            total += digit * 10 ** (n - 1 - i) * perm
        results.append(str(total))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()