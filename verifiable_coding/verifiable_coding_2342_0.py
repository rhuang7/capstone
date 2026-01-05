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
        # The key observation is that the array must be non-decreasing
        # and the sum of the first i elements must be less than or equal to the sum of the first i elements of the original array
        # This is because we can only decrement the first k or last k elements
        # So the prefix sums must be non-decreasing
        prefix_sum = 0
        for i in range(n):
            prefix_sum += a[i]
            if prefix_sum < 0:
                results.append("NO")
                break
        else:
            results.append("YES")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()