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
        max_size = 0
        current = 0
        
        for i in range(len(values)):
            if current >= values[i]:
                # Cannot take this frequency, break
                break
            # Take as many as possible without exceeding the current count
            take = min(values[i], current + 1)
            max_size += take
            current += 1
        
        results.append(str(max_size))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()