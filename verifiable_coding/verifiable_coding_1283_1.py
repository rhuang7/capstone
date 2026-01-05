import sys

def is_semi_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i != n // i:
                return True
            else:
                return False
    return False

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        possible = False
        for a in range(2, N // 2 + 1):
            if is_semi_prime(a):
                for b in range(2, N - a + 1):
                    if is_semi_prime(b):
                        if a + b == N:
                            possible = True
                            break
                if possible:
                    break
        results.append("YES" if possible else "NO")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()