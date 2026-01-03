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
        N, H = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Binary search for the minimum K
        left = 1
        right = max(A)
        answer = right
        
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for a in A:
                hours += a // mid
                if a % mid != 0:
                    hours += 1
                if hours > H:
                    break
            if hours <= H:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        results.append(answer)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()