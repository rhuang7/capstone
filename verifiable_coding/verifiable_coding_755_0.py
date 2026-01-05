import sys

def solve():
    import math
    data = sys.stdin.buffer.read().split()
    M = int(data[0])
    arr = list(map(int, data[1:M+1]))
    
    # Compute the gcd of all elements
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    current_gcd = arr[0]
    for num in arr[1:]:
        current_gcd = gcd(current_gcd, num)
    
    # Find all divisors of current_gcd that are > 1
    def get_divisors(n):
        divisors = set()
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                divisors.add(i)
                if n // i > 1:
                    divisors.add(n // i)
        if n > 1:
            divisors.add(n)
        return sorted(divisors)
    
    result = get_divisors(current_gcd)
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()