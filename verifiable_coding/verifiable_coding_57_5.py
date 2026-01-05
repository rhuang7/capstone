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
        
        # We can always remove elements until one remains if there is at least one increasing pair
        # But we need to check if there is a way to remove elements such that we can keep reducing until one remains
        # The key observation is that if the array is strictly increasing, we can remove elements from the end
        # If the array is not strictly increasing, then there is at least one place where a[i] < a[i+1], and we can remove one of them
        # So the answer is always "YES" unless the array is strictly decreasing
        is_increasing = True
        for i in range(n - 1):
            if a[i] >= a[i + 1]:
                is_increasing = False
                break
        if is_increasing:
            results.append("NO")
        else:
            results.append("YES")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()