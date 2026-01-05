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
        
        # We need to check if the array can be reduced to all zeros
        # by applying the allowed operations
        # The key insight is that the prefix sums must be non-decreasing
        # and the total sum must be equal to the sum of the prefix sums
        
        prefix_sum = 0
        total_sum = 0
        
        for i in range(n):
            total_sum += a[i]
            prefix_sum += a[i]
            if i > 0:
                if prefix_sum < previous_prefix_sum:
                    results.append("NO")
                    break
            previous_prefix_sum = prefix_sum
        
        if all(a[i] == 0 for i in range(n)):
            results.append("YES")
        else:
            results.append("YES" if total_sum == prefix_sum else "NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()