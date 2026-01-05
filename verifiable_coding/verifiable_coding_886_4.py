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
        a = list(map(int, data[idx:idx+N]))
        idx += N
        M = int(data[idx])
        idx += 1
        
        # Step 1: swap every alternate number with its succeeding number
        for i in range(0, N-1, 2):
            a[i], a[i+1] = a[i+1], a[i]
        
        # Step 2: add %3 of every number to itself
        for i in range(N):
            a[i] += a[i] % 3
        
        # Step 3: swap ith number and (N-i-1)th number
        for i in range(N // 2):
            a[i], a[N - i - 1] = a[N - i - 1], a[i]
        
        # Find nearest smaller and greater
        smaller = -1
        greater = -1
        for num in a:
            if num < M and smaller == -1:
                smaller = num
            elif num > M and greater == -1:
                greater = num
        results.append(f"{smaller} {greater}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()