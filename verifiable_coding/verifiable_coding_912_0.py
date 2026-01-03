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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        x = list(map(int, data[idx:idx+n]))
        idx += n
        
        x.sort()
        
        low = 0
        high = x[-1] - x[0]
        
        def is_possible(distance):
            count = 1
            last = x[0]
            for pos in x[1:]:
                if pos - last >= distance:
                    count += 1
                    last = pos
                    if count == k:
                        return True
            return False
        
        while low < high:
            mid = (low + high + 1) // 2
            if is_possible(mid):
                low = mid
            else:
                high = mid - 1
        
        results.append(low)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()