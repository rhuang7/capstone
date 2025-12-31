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
        
        # Calculate how much we can move to pile 1
        max_haybales = a[0]
        remaining_days = d
        
        for i in range(1, n):
            # Calculate the number of days needed to move all haybales from pile i to pile i-1
            days_needed = a[i] * i
            if remaining_days >= days_needed:
                max_haybales += a[i]
                remaining_days -= days_needed
            else:
                # We can only move some haybales
                max_haybales += remaining_days // i
                remaining_days = 0
                break
        
        results.append(str(max_haybales))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()