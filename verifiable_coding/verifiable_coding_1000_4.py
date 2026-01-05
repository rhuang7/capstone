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
        # and check if total is divisible by N
        if total % N == 0:
            results.append(total // N)
        else:
            results.append(total // N + 1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()