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
        N, K, V = map(int, data[idx:idx+3])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        total_remaining = sum(A)
        total_original = (N + K) * V
        
        if total_original - total_remaining < 0:
            results.append(-1)
            continue
        
        x = (total_original - total_remaining) // K
        if (total_original - total_remaining) % K != 0 or x <= 0:
            results.append(-1)
        else:
            results.append(x)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()