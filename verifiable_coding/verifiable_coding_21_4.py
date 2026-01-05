import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        s = list(map(int, data[idx:idx + n]))
        idx += n
        
        original_set = set(s)
        found = False
        for k in range(1, 1024):
            new_set = set()
            for num in s:
                new_set.add(num ^ k)
            if new_set == original_set:
                results.append(str(k))
                found = True
                break
        if not found:
            results.append("-1")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()