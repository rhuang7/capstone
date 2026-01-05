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
        
        # Sort the frequencies in descending order
        values.sort(reverse=True)
        
        # Try to assign the maximum possible distinct counts
        res = 0
        count = 0
        
        for i in range(len(values)):
            # We can take at most min(current count + 1, values[i]) of this type
            take = min(count + 1, values[i])
            res += take
            count += 1
        
        results.append(str(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()