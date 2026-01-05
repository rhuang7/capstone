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
        n, m = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+m]))
        idx += m
        
        pos = {present: i for i, present in enumerate(a)}
        
        time = 0
        last = -1
        
        for i in range(m):
            current = b[i]
            p = pos[current]
            if p < last:
                time += 2 * (p - last) + 1
            else:
                time += 2 * (p - last) + 1
            last = p
        
        results.append(time)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()