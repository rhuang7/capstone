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
        
        # Calculate the difference between each pair of consecutive plants
        diff = [A[i] - A[i+1] for i in range(N-1)]
        
        # Find the minimum time when any two plants have the same height
        # The time for plant i and plant j (i < j) to have same height is (A[i] - A[j]) / (j - i)
        # We need to find the minimum such time
        min_time = float('inf')
        
        for i in range(N-1):
            for j in range(i+1, N):
                if diff[j - i - 1] == 0:
                    min_time = 0
                    break
                if diff[j - i - 1] < 0:
                    continue
                time = diff[j - i - 1] // (j - i)
                if diff[j - i - 1] % (j - i) != 0:
                    time += 1
                if time < min_time:
                    min_time = time
            if min_time == 0:
                break
        
        results.append(str(min_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()