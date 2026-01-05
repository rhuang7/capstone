import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
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
        for z in range(1, 10000):
            if is_prime(total + z):
                print(z)
                break

if __name__ == '__main__':
    solve()