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
            # Calculate how many days are needed to move all haybales from pile i to pile 1
            days_needed = a[i] * i
            if days_needed <= d:
                max_haybales += a[i]
                d -= days_needed
            else:
                # Can only move some haybales
                max_haybales += d // i
                d = 0
                break
        
        results.append(str(max_haybales))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()