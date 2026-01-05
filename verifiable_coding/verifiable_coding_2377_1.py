import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        sorted_a = sorted(a)
        pos = [0] * n
        for i in range(n):
            pos[i] = sorted_a.index(a[i])
        
        res = 0
        last = 0
        for i in range(n):
            if pos[i] < last:
                res += 1
            else:
                last = pos[i]
        
        print(res)

if __name__ == '__main__':
    solve()