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
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        sorted_a = sorted(a)
        pos = [0] * n
        for i in range(n):
            pos[i] = sorted_a.index(a[i])
        
        max_len = 0
        current_len = 0
        for i in range(n):
            if i == 0 or pos[i] == pos[i-1] + 1:
                current_len += 1
            else:
                current_len = 1
            max_len = max(max_len, current_len)
        
        results.append(n - max_len)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()