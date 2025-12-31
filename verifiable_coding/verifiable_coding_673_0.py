import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index+1])
        a = int(data[index+2])
        d = int(data[index+3])
        index += 4
        
        # Generate the 5 divisors
        divisors = [a + i*d for i in range(5)]
        
        # Use inclusion-exclusion principle to count numbers not divisible by any of the divisors
        # Total numbers in range: m - n + 1
        total = m - n + 1
        
        # Count numbers divisible by at least one of the divisors
        # Using inclusion-exclusion for 5 sets
        # This is a simplified version for 5 elements, but for larger numbers it would be better to use a sieve or other method
        
        # We'll use a set to store the numbers in the range [n, m]
        # But for large ranges, this is not feasible, so we use inclusion-exclusion
        # Here we use inclusion-exclusion for 5 elements
        
        # Count numbers divisible by each divisor
        cnt = 0
        for x in divisors:
            cnt += (m // x) - ((n - 1) // x)
        
        # Subtract numbers divisible by pairwise LCMs
        for i in range(5):
            for j in range(i + 1, 5):
                l = divisors[i] * divisors[j]
                if l > m:
                    continue
                cnt -= (m // l) - ((n - 1) // l)
        
        # Add numbers divisible by triple LCMs
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    l = divisors[i] * divisors[j] * divisors[k]
                    if l > m:
                        continue
                    cnt += (m // l) - ((n - 1) // l)
        
        # Subtract numbers divisible by quadruple LCMs
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    for l in range(k + 1, 5):
                        lcm = divisors[i] * divisors[j] * divisors[k] * divisors[l]
                        if lcm > m:
                            continue
                        cnt -= (m // lcm) - ((n - 1) // lcm)
        
        # Add numbers divisible by all 5 LCMs
        lcm = divisors[0] * divisors[1] * divisors[2] * divisors[3] * divisors[4]
        if lcm <= m:
            cnt += (m // lcm) - ((n - 1) // lcm)
        
        # The answer is total - cnt
        print(total - cnt)

if __name__ == '__main__':
    solve()