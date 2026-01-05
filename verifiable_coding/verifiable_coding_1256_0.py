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
        
        count = 0
        # Count pairs (i, j) where i < j and A[i] * A[j] > A[i] + A[j]
        # The inequality A[i] * A[j] > A[i] + A[j] is equivalent to (A[i] - 1) * (A[j] - 1) > 1
        # So we count pairs where (A[i] - 1) * (A[j] - 1) > 1
        # This is true when both A[i] and A[j] are >= 2
        # So we count the number of elements >= 2, and compute combinations of 2
        cnt = 0
        for num in A:
            if num >= 2:
                cnt += 1
        # Total pairs with both elements >= 2 is cnt * (cnt - 1) // 2
        results.append(cnt * (cnt - 1) // 2)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()