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
        
        # Find all increasing runs
        increasing_runs = []
        i = 0
        while i < N:
            j = i
            while j + 1 < N and A[j] < A[j + 1]:
                j += 1
            increasing_runs.append(j - i + 1)
            i = j + 1
        
        # Calculate the number of valid subarrays
        total = 0
        for run in increasing_runs:
            total += run * (run + 1) // 2
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()