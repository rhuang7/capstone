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
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        min_diff = float('inf')
        count = 0
        
        a.sort()
        
        for i in range(N):
            left = i + 1
            right = N - 1
            while left <= right:
                current_sum = a[i] + a[left]
                diff = abs(current_sum - K)
                if diff < min_diff:
                    min_diff = diff
                    count = 1
                elif diff == min_diff:
                    count += 1
                if current_sum < K:
                    left += 1
                else:
                    right -= 1
        
        results.append(f"{min_diff} {count}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()