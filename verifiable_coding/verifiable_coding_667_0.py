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
        
        # Find the latest day Y such that Y is a multiple of X[0], and there exists a day >= Y for each subsequent X[i]
        # The latest possible Y is the maximum multiple of X[0] that is <= D and such that D >= (Y // X[0]) * X[0] and D >= (Y // X[1]) * X[1], etc.
        
        # We can use binary search to find the latest Y
        low = 1
        high = D
        answer = 0
        
        while low <= high:
            mid = (low + high) // 2
            valid = True
            for x in X:
                if mid % x != 0:
                    valid = False
                    break
            if valid:
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        
        results.append(str(answer))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()