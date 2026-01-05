import sys

def solve():
    import math
    data = sys.stdin.buffer.read().split()
    M = int(data[0])
    arr = list(map(int, data[1:M+1]))
    
    # Compute the GCD of all elements
    gcd_val = arr[0]
    for num in arr[1:]:
        gcd_val = math.gcd(gcd_val, num)
    
    # Find all divisors of gcd_val that are > 1
    divisors = set()
    for i in range(2, int(math.isqrt(gcd_val)) + 1):
        if gcd_val % i == 0:
            divisors.add(i)
            if i != gcd_val // i:
                divisors.add(gcd_val // i)
    if gcd_val > 1:
        divisors.add(gcd_val)
    
    # Sort the divisors
    sorted_divisors = sorted(divisors)
    
    # Output the result
    print(' '.join(map(str, sorted_divisors)))

if __name__ == '__main__':
    solve()