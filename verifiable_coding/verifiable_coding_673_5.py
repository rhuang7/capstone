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
        divisors = [a + i*d for i in range(5)]
        
        # Use inclusion-exclusion principle to count numbers divisible by any of the divisors
        # Total numbers in range: m - n + 1
        total = m - n + 1
        
        # Count numbers divisible by at least one of the divisors
        count = 0
        for i in range(5):
            count += (m // divisors[i]) - ((n - 1) // divisors[i])
        for i in range(5):
            for j in range(i + 1, 5):
                count -= (m // (divisors[i] * divisors[j])) - ((n - 1) // (divisors[i] * divisors[j]))
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    count -= (m // (divisors[i] * divisors[j] * divisors[k])) - ((n - 1) // (divisors[i] * divisors[j] * divisors[k]))
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    for l in range(k + 1, 5):
                        count -= (m // (divisors[i] * divisors[j] * divisors[k] * divisors[l])) - ((n - 1) // (divisors[i] * divisors[j] * divisors[k] * divisors[l]))
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    for l in range(k + 1, 5):
                        for m in range(l + 1, 5):
                            count -= (m // (divisors[i] * divisors[j] * divisors[k] * divisors[l] * divisors[m])) - ((n - 1) // (divisors[i] * divisors[j] * divisors[k] * divisors[l] * divisors[m]))
        
        # The answer is total - count
        results.append(str(total - count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()