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
        n = N
        total = 0
        for i in range(n):
            digit = digits[i]
            count = 1
            for j in range(i + 1, n):
                if digits[j] == digit:
                    count += 1
            place = 10 ** (n - i - 1)
            total += digit * count * (10 ** (n - i - 1)) * (sum(10 ** (n - i - 1 - k) for k in range(n - i)) // (10 ** (n - i)) * (sum(10 ** (n - i - 1 - k) for k in range(n - i)) // (10 ** (n - i)) + 1) // 2))
        results.append(str(total))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()