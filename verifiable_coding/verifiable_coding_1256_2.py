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
        # The inequality can be rewritten as (A[i] - 1) * (A[j] - 1) > 0
        # So, A[i] > 1 and A[j] > 1
        # So we count the number of elements > 1, then compute combinations
        cnt = 0
        for num in A:
            if num > 1:
                cnt += 1
        # Number of valid pairs is C(cnt, 2) = cnt * (cnt - 1) // 2
        results.append(cnt * (cnt - 1) // 2)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()