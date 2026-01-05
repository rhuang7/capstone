import sys

def solve():
    import math
    data = sys.stdin.buffer.read().split()
    M = int(data[0])
    arr = list(map(int, data[1:M+1]))
    
    # Find the GCD of all elements
    gcd = arr[0]
    for num in arr[1:]:
        gcd = math.gcd(gcd, num)
    
    # Find all divisors of the GCD greater than 1
    divisors = set()
    for i in range(2, int(math.isqrt(gcd)) + 1):
        if gcd % i == 0:
            divisors.add(i)
            if i != gcd // i:
                divisors.add(gcd // i)
    if gcd > 1:
        divisors.add(gcd)
    
    # Sort the divisors
    result = sorted(divisors)
    
    # Print the result
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()