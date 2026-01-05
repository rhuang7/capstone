import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        n = len(s)
        res = list(s)
        possible = True
        
        for i in range(n // 2):
            if res[i] == '.':
                res[i] = res[n - 1 - i]
            elif res[i] != res[n - 1 - i]:
                possible = False
                break
        
        if not possible:
            print(-1)
            continue
        
        for i in range(n // 2, n):
            if res[i] == '.':
                res[i] = res[n - 1 - i]
        
        print(''.join(res))
        
if __name__ == '__main__':
    solve()