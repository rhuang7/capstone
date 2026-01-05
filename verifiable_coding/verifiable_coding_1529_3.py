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
            total += digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n - 1 - i)) * (count * (count - 1) // 2) * (10 ** (n - 1)) + digit * (10 ** (n -