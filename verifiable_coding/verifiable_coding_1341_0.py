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
        
        # Compute the number of valid contiguous subarrays that are strictly increasing
        # and ensure the remaining sequence is non-empty
        count = 0
        increasing = 1
        for i in range(1, N):
            if A[i] > A[i-1]:
                increasing += 1
            else:
                increasing = 1
            count += increasing
        
        # Subtract the cases where the entire array is removed (which is not allowed)
        # and add the cases where the entire array is kept (which is allowed)
        # But we need to ensure the remaining sequence is non-empty
        # So the total is count - (N - 1) + 1 (if the entire array is increasing)
        # But we need to check if the entire array is strictly increasing
        is_increasing = True
        for i in range(1, N):
            if A[i] <= A[i-1]:
                is_increasing = False
                break
        if is_increasing:
            count -= (N - 1)
            count += 1
        else:
            count -= (N - 1)
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()