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
        
        # We can always reduce the array to 1 element if there is at least one increasing pair
        # because we can always remove one element from an increasing pair
        # However, if the array is strictly decreasing, we cannot perform any operation
        # So check if the array is strictly decreasing
        is_decreasing = True
        for i in range(n - 1):
            if a[i] < a[i + 1]:
                is_decreasing = False
                break
        if is_decreasing:
            results.append("NO")
        else:
            results.append("YES")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()