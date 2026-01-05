import sys

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        n = int(data[i])
        total = 0
        for j in range(2, n + 1):
            if is_prime(j):
                total += j
        results.append(str(total % 10))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()