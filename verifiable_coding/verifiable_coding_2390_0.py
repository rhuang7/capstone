import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    q = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        freq = collections.Counter(a)
        values = list(freq.values())
        values.sort(reverse=True)
        
        res = 0
        i = 0
        while i < len(values):
            if res + 1 <= values[i]:
                res += 1
                i += 1
            else:
                i += 1
        results.append(str(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()