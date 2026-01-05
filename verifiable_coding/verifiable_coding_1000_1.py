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
        # But since we can't have fractional speed, we need to compute it properly
        # speed = (total + N - 1) // N
        # But we need to ensure that the speed is such that the total time is at least the sum of all A_i
        # So the minimum speed is the ceiling of (sum(A) / N)
        speed = (total + N - 1) // N
        results.append(str(speed))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()