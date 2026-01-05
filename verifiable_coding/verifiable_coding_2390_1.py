import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    q = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(q):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        count = collections.Counter(a)
        values = sorted(count.values(), reverse=True)
        
        res = 0
        i = 0
        while i < len(values):
            if res + 1 <= values[i]:
                res += 1
                i += 1
            else:
                res += values[i]
                i += 1
        
        results.append(str(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()