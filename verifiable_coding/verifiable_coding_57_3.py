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
        # Because we can always remove one element from an increasing pair
        # However, if the array is strictly decreasing, we cannot do anything
        # So check if there is at least one increasing pair
        can_reduce = False
        for i in range(n - 1):
            if a[i] < a[i + 1]:
                can_reduce = True
                break
        
        results.append("YES" if can_reduce else "NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()