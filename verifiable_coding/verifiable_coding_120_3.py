import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        if m == 0:
            results.append(0)
            continue
        
        # The maximum value of f(s) is achieved when the '1's are spread as much as possible
        # to maximize the number of substrings containing at least one '1'
        # The formula is: (n - m) * (n - m + 1) // 2 + m * (m + 1) // 2 + m * (n - m)
        # Which simplifies to: (n * (n + 1) // 2) - ( (n - m) * (n - m + 1) // 2 )
        total = n * (n + 1) // 2
        zeros = n - m
        total -= zeros * (zeros + 1) // 2
        
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()