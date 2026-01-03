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
        
        # Calculate the minimum speed
        total_time = 0
        current_time = 0
        for a in A:
            total_time += a
            if current_time >= total_time:
                current_time = 0
            else:
                current_time += a
        
        # The minimum speed is ceil(total_time / N)
        # But since we can't have fractional speed, we need to find the smallest integer s such that s * N >= total_time
        # So s = ceil(total_time / N)
        # But since we can't use math.ceil, we compute it as (total_time + N - 1) // N
        speed = (total_time + N - 1) // N
        results.append(str(speed))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()