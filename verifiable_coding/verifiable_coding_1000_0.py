import sys

def solve():
    import math
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
        
        # Calculate the minimum speed using binary search
        left = 1
        right = 10**18
        answer = 0
        
        while left <= right:
            mid = (left + right) // 2
            total_time = 0
            current_time = 0
            for a in A:
                if current_time >= a * mid:
                    current_time = 0
                current_time += a * mid
                total_time = max(total_time, current_time)
            
            if total_time <= N * mid:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        results.append(answer)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()