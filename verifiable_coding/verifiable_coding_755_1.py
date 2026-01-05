import sys

def solve():
    import math
    data = sys.stdin.buffer.read().split()
    M = int(data[0])
    arr = list(map(int, data[1:M+1]))
    
    # Compute the GCD of all elements
    gcd_all = arr[0]
    for num in arr[1:]:
        gcd_all = math.gcd(gcd_all, num)
    
    # Find all divisors of gcd_all that are >1
    divisors = set()
    for i in range(2, int(math.isqrt(gcd_all)) + 1):
        if gcd_all % i == 0:
            divisors.add(i)
            if i != gcd_all // i:
                divisors.add(gcd_all // i)
    divisors.add(gcd_all)
    
    # Sort the divisors
    result = sorted(divisors)
    
    # Print the result
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()