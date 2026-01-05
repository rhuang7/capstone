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
        n = int(data[idx])
        idx += 1
        x = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx + n]))
        idx += n
        
        A.sort()
        
        day = 1
        count = 0
        
        for a in A:
            if a > day:
                day += 1
            else:
                count += 1
                if count == x:
                    count = 0
                    day += 1
        
        if count == 0:
            results.append("Possible")
        else:
            results.append("Impossible")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()