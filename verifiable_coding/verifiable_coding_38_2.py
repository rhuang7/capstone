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
        # because they can always play that card to win each round
        # So the player with the maximum card wins
        max_a = max(a)
        max_b = max(b)
        
        if max_a > max_b:
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()