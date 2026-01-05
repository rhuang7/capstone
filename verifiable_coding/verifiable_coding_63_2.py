import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        w = list(map(int, data[idx:idx+k]))
        idx += k
        
        a.sort()
        w.sort(reverse=True)
        
        total = 0
        # Assign the largest elements as max for each friend
        for i in range(k):
            total += a[-1]
            a.pop()
            # Assign the smallest element as min for each friend
            total += a[0]
            a.pop(0)
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()