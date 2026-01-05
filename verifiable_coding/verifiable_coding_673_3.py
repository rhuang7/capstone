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
        
        # Compute the 5 values: a, a+d, a+2d, a+3d, a+4d
        values = [a + i*d for i in range(5)]
        
        # Use inclusion-exclusion principle to count numbers divisible by any of the values
        # Total numbers in range: m - n + 1
        total = m - n + 1
        
        # Count numbers divisible by each value
        cnt = [0] * 5
        for i in range(5):
            cnt[i] = (m // values[i]) - ((n - 1) // values[i])
        
        # Inclusion-exclusion
        # Add single sets
        res = sum(cnt)
        
        # Subtract pairwise intersections
        for i in range(5):
            for j in range(i+1, 5):
                res -= (m // (values[i] * values[j])) - ((n - 1) // (values[i] * values[j]))
        
        # Add triple intersections
        for i in range(5):
            for j in range(i+1, 5):
                for k in range(j+1, 5):
                    res += (m // (values[i] * values[j] * values[k])) - ((n - 1) // (values[i] * values[j] * values[k]))
        
        # Subtract four-way intersections
        for i in range(5):
            for j in range(i+1, 5):
                for k in range(j+1, 5):
                    for l in range(k+1, 5):
                        res -= (m // (values[i] * values[j] * values[k] * values[l])) - ((n - 1) // (values[i] * values[j] * values[k] * values[l]))
        
        # Add five-way intersection
        for i in range(5):
            for j in range(i+1, 5):
                for k in range(j+1, 5):
                    for l in range(k+1, 5):
                        for p in range(l+1, 5):
                            res += (m // (values[i] * values[j] * values[k] * values[l] * values[p])) - ((n - 1) // (values[i] * values[j] * values[k] * values[l] * values[p]))
        
        # The answer is total - res
        print(total - res)

if __name__ == '__main__':
    solve()