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
        
        def can_finish(K):
            hours = 0
            for a in A:
                hours += a // K
                if a % K != 0:
                    hours += 1
                if hours > H:
                    return False
            return hours <= H
        
        low = 1
        high = max(A)
        answer = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_finish(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        results.append(answer)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()