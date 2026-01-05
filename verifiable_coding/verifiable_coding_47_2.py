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
        n, q = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        # Compute max strength
        # The maximum alternating sum is achieved by taking the largest elements in a way that maximizes the sum
        # We sort the array and take the largest elements, alternating signs
        # The optimal strategy is to take the largest element, then the smallest, then the next largest, etc.
        # So we sort the array and take the largest elements in a way that alternates between positive and negative
        # We can do this by sorting the array and then taking the largest elements in a way that alternates between positive and negative
        # Let's sort the array
        a.sort()
        # Now, we take the largest elements in a way that alternates between positive and negative
        # We start with positive
        max_strength = 0
        sign = 1
        for i in range(n-1, -1, -1):
            if sign == 1:
                max_strength += a[i]
            else:
                max_strength -= a[i]
            sign *= -1
        results.append(str(max_strength))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()