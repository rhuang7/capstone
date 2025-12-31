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
        a = list(map(int, data[idx:idx + 2 * n]))
        idx += 2 * n
        
        a.sort()
        
        # The optimal way is to have classes of sizes 1 and 2n-1, or 2n-1 and 1
        # The medians will be a[0] and a[2n-1], or a[2n-1] and a[0]
        # The minimal difference is the absolute difference between a[0] and a[2n-1]
        # But wait, there's another possibility: classes of sizes 3 and 2n-3
        # The medians will be a[1] and a[2n-2], or a[2n-2] and a[1]
        # So we need to compare all possible medians of classes of odd sizes
        
        # The minimal difference is between the two middle elements of the sorted array
        # Because the optimal way is to split the array into two parts with medians as close as possible
        # The minimal difference is the difference between the middle elements of the sorted array
        # For 2n elements, the middle elements are at positions n-1 and n (0-based)
        # So the minimal difference is a[n] - a[n-1]
        min_diff = a[n] - a[n-1]
        results.append(str(min_diff))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()