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
        # Compute maximum strength
        # The maximum strength is achieved by choosing the largest element
        # and then the next largest element, and so on, alternating signs
        # So we sort the array and take the largest, then the next largest,
        # then the next, etc., alternating signs
        a.sort()
        max_strength = 0
        for i in range(n):
            if i % 2 == 0:
                max_strength += a[i]
            else:
                max_strength -= a[i]
        results.append(str(max_strength))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()