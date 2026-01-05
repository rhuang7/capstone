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
        
        # We can always reduce the array to one element if there is at least one increasing pair
        # because we can always remove the larger element in an increasing pair
        # So the answer is "YES" if there is at least one increasing pair
        # Otherwise, it's "NO"
        possible = False
        for i in range(n - 1):
            if a[i] < a[i + 1]:
                possible = True
                break
        results.append("YES" if possible else "NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()