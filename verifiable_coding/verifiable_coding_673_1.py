import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        a = int(data[idx+2])
        d = int(data[idx+3])
        idx += 4
        
        # Compute the 5 values: a, a+d, a+2d, a+3d, a+4d
        values = [a + i*d for i in range(5)]
        
        # Use inclusion-exclusion principle to count numbers divisible by any of the values
        # Total numbers in range [n, m] = m - n + 1
        total = m - n + 1
        
        # Count numbers divisible by each value
        count = 0
        for val in values:
            count += (m // val) - ((n - 1) // val)
        
        # Subtract numbers divisible by intersections of two values
        for i in range(5):
            for j in range(i+1, 5):
                l = values[i]
                r = values[j]
                lcm = l * r // (l // r)
                count -= (m // lcm) - ((n - 1) // lcm)
        
        # Add back numbers divisible by intersections of three values
        for i in range(5):
            for j in range(i+1, 5):
                for k in range(j+1, 5):
                    l = values[i]
                    m_val = values[j]
                    n_val = values[k]
                    lcm1 = l * m_val // (l // m_val)
                    lcm2 = lcm1 * n_val // (lcm1 // n_val)
                    count += (m // lcm2) - ((n - 1) // lcm2)
        
        # Subtract numbers divisible by intersections of four values
        for i in range(5):
            for j in range(i+1, 5):
                for k in range(j+1, 5):
                    for l in range(k+1, 5):
                        val1 = values[i]
                        val2 = values[j]
                        val3 = values[k]
                        val4 = values[l]
                        lcm1 = val1 * val2 // (val1 // val2)
                        lcm2 = lcm1 * val3 // (lcm1 // val3)
                        lcm3 = lcm2 * val4 // (lcm2 // val4)
                        count -= (m // lcm3) - ((n - 1) // lcm3)
        
        # Add back numbers divisible by intersections of five values
        lcm = 1
        for val in values:
            lcm = lcm * val // (lcm // val)
        count += (m // lcm) - ((n - 1) // lcm)
        
        # The answer is total - count
        print(total - count)

if __name__ == '__main__':
    solve()