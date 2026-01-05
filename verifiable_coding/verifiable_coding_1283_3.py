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
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    semi_primes = set()
    for i in range(2, 200):
        if is_semi_prime(i):
            semi_primes.add(i)
    
    for N in cases:
        found = False
        for a in semi_primes:
            if a > N:
                break
            if (N - a) in semi_primes:
                found = True
                break
        print("YES" if found else "NO")

if __name__ == '__main__':
    solve()