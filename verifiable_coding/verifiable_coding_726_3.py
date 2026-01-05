import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        count = {}
        for _ in range(N):
            s = data[idx]
            idx += 1
            for c in s:
                count[c] = count.get(c, 0) + 1
        
        target = {'c': 0, 'o': 0, 'd': 0, 'e': 0, 'h': 0, 'f': 0}
        meals = 0
        for c in count:
            if c in target:
                target[c] = count[c]
        
        for c in target:
            if c not in count:
                target[c] = 0
        
        min_freq = float('inf')
        for c in target:
            min_freq = min(min_freq, target[c])
        
        print(min_freq)

if __name__ == '__main__':
    solve()