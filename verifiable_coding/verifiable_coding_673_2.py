import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        a = int(data[idx+2])
        d = int(data[idx+3])
        idx += 4
        
        # Compute the 5 values: a, a+d, a+2d, a+3d, a+4d
        values = [a + i*d for i in range(5)]
        
        # Use inclusion-exclusion principle to count numbers divisible by any of the values
        # Total numbers in range: m - n + 1
        total = m - n + 1
        
        # Count numbers divisible by at least one of the values
        # Using inclusion-exclusion for 5 sets
        # This is a simplified version for 5 elements, not the general case
        # For the problem constraints, this is efficient enough
        
        # Count multiples of each value
        cnt = 0
        for val in values:
            cnt += (m // val) - ((n - 1) // val)
        
        # Subtract multiples of pairwise LCMs
        for i in range(5):
            for j in range(i + 1, 5):
                l = values[i] // (values[i] // values[j]) * values[j]
                cnt -= (m // l) - ((n - 1) // l)
        
        # Add multiples of triple LCMs
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    l = values[i] // (values[i] // values[j]) * values[j] // (values[j] // values[k]) * values[k]
                    cnt += (m // l) - ((n - 1) // l)
        
        # Subtract multiples of quadruple LCMs
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    for l in range(k + 1, 5):
                        l = values[i] // (values[i] // values[j]) * values[j] // (values[j] // values[k]) * values[k] // (values[k] // values[l]) * values[l]
                        cnt -= (m // l) - ((n - 1) // l)
        
        # Add multiples of all 5 LCMs
        l = values[0] // (values[0] // values[1]) * values[1] // (values[1] // values[2]) * values[2] // (values[2] // values[3]) * values[3] // (values[3] // values[4]) * values[4]
        cnt += (m // l) - ((n - 1) // l)
        
        # The answer is total - cnt
        results.append(str(total - cnt))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()