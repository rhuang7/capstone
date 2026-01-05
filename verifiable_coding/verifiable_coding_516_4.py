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
        
        # Compute inversions in original array A
        inv_in_A = 0
        for i in range(N):
            for j in range(i+1, N):
                if A[i] > A[j]:
                    inv_in_A += 1
        
        # Compute inversions between copies
        inv_between_copies = 0
        for i in range(N):
            for j in range(i+1, N):
                if A[i] > A[j]:
                    inv_between_copies += K * (K - 1)
        
        # Compute inversions within copies
        inv_within_copies = inv_in_A * K
        
        total_inversions = inv_within_copies + inv_between_copies
        results.append(total_inversions)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()