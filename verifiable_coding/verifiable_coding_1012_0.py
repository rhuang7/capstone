import sys
MOD = 10**9 + 7

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def char_value(c):
    return ord(c) - ord('a')

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    strings = data[1:T+1]
    
    primes = [i for i in range(2, 100) if is_prime(i)]
    
    for s in strings:
        n = len(s)
        prime_positions = [i for i in range(n) if is_prime(i+1)]
        total = 0
        for i in range(n):
            if is_prime(i+1):
                total += char_value(s[i])
        if is_prime(total):
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    solve()