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
        # We can always reduce to one element if there is at least one increasing pair
        # But we need to check if there's a way to remove elements such that we can keep going
        # The key observation is that if there is at least one increasing pair, we can always reduce to one element
        # Because we can always remove the larger element in an increasing pair
        # So the answer is YES if there is at least one increasing pair
        # Otherwise, it's NO
        
        # Check if there is at least one increasing pair
        possible = False
        for i in range(n - 1):
            if a[i] < a[i + 1]:
                possible = True
                break
        
        results.append("YES" if possible else "NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()