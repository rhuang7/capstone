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
        k1 = int(data[idx+1])
        k2 = int(data[idx+2])
        idx += 3
        
        a = list(map(int, data[idx:idx+k1]))
        idx += k1
        b = list(map(int, data[idx:idx+k2]))
        idx += k2
        
        a.sort()
        b.sort()
        
        # The player with the highest card can always win
        # because they can always play their highest card to win
        # and repeat the process
        if a[-1] > b[-1]:
            results.append("YES")
        else:
            results.append("NO")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()