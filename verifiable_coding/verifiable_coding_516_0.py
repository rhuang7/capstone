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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute inversions in original array
        inv_original = 0
        for i in range(N):
            for j in range(i+1, N):
                if A[i] > A[j]:
                    inv_original += 1
        
        # Compute inversions between copies
        inv_between = 0
        for i in range(N):
            for j in range(i+1, N):
                if A[i] > A[j]:
                    inv_between += K * (K - 1) // 2
        
        # Compute inversions within copies
        inv_within = inv_original * K * (K - 1) // 2
        
        total = inv_original * K + inv_between + inv_within
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()