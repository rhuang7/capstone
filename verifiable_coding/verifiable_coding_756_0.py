import sys

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        x = int(input[idx])
        y = int(input[idx+1])
        idx += 2
        total = x + y
        z = 1
        while True:
            if is_prime(total + z):
                print(z)
                break
            z += 1

if __name__ == '__main__':
    solve()