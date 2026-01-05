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
        N, D = int(data[idx]), int(data[idx+1])
        idx += 2
        X = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Find the latest day Y such that Y is a multiple of X[0], and there exists a day >= Y for each subsequent X[i] that is <= D
        # We can use binary search on Y
        low = 1
        high = D
        answer = 1
        
        while low <= high:
            mid = (low + high) // 2
            # Check if it's possible to take the first bus on day mid and finish by day D
            # For each X[i], the earliest day after mid that is a multiple of X[i] is ceil(mid / X[i]) * X[i]
            # This must be <= D
            possible = True
            for xi in X:
                if mid % xi != 0:
                    next_day = (mid // xi) + 1
                    next_day *= xi
                    if next_day > D:
                        possible = False
                        break
            if possible:
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        
        results.append(str(answer))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()