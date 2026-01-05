import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        total = 0
        for a in A:
            total += a
        
        # The minimum speed is the ceiling of total / N
        # But since we can't have fractional speed, we use integer division
        # To compute ceiling(a / b) when a and b are positive integers:
        # ceiling(a / b) = (a + b - 1) // b
        speed = (total + N - 1) // N
        results.append(str(speed))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()