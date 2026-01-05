import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Check if it's possible to make all elements zero
        # The key observation is that for each position i, the value a[i] must be less than or equal to the sum of the first i elements
        # and also less than or equal to the sum of the last (n - i) elements
        # This is because we can only decrease elements from the front or the back
        # So for each i, a[i] <= prefix_sum[i] and a[i] <= suffix_sum[n - i - 1]
        prefix_sum = [0] * (n + 1)
        suffix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + a[i]
            suffix_sum[n - i - 1] = suffix_sum[n - i] + a[i]
        
        possible = True
        for i in range(n):
            if a[i] > prefix_sum[i] or a[i] > suffix_sum[n - i - 1]:
                possible = False
                break
        
        results.append("YES" if possible else "NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()