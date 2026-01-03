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
        
        # Check if the array can be reduced to one element
        # The key observation is that if there is at least one pair (i, i+1) where a[i] < a[i+1], then it is possible
        # because we can always remove one element from such a pair
        # However, if the array is strictly decreasing, then no such pair exists, and it is impossible
        possible = False
        for i in range(n - 1):
            if a[i] < a[i + 1]:
                possible = True
                break
        
        results.append("YES" if possible else "NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()