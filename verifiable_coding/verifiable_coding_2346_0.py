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
        n, d = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Calculate the maximum possible haybales in pile 1
        max_haybales = 0
        for i in range(1, n):
            # How many days can we move haybales from pile i to pile 1
            # Each haybale from pile i takes i days to reach pile 1
            # So, we can move min(d // i, a[i-1]) haybales
            days_per_haybale = i
            max_possible = min(d // days_per_haybale, a[i-1])
            max_haybales += max_possible
            d -= max_possible * days_per_haybale
        
        results.append(str(max_haybales))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()