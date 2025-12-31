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
        
        deleted_total = total_original - total_remaining
        
        if deleted_total < 0:
            results.append(-1)
            continue
        
        if deleted_total % K != 0:
            results.append(-1)
            continue
        
        deleted_value = deleted_total // K
        
        if deleted_value <= 0:
            results.append(-1)
        else:
            results.append(deleted_value)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()