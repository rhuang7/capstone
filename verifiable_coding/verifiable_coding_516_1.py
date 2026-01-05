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
        
        inversions = 0
        
        # Count inversions within one copy of A
        for i in range(N):
            for j in range(i+1, N):
                if A[i] > A[j]:
                    inversions += 1
        
        # Count inversions between different copies
        # For each pair (i, j) where i < j in the original array
        # There are K*(K-1) such pairs across all copies
        # Each such pair contributes to inversions if A[i] > A[j]
        # So we count the number of such pairs in A and multiply by K*(K-1)
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                if A[i] > A[j]:
                    count += 1
        inversions += count * K * (K - 1)
        
        results.append(inversions)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()