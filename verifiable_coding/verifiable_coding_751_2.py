import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        x = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Find positions of villages with electricity
        has_electricity = [i for i in range(n) if s[i] == '1']
        # Find the first and last village with electricity
        first = has_electricity[0]
        last = has_electricity[-1]
        
        # The minimum wire length is the distance between the first and last village with electricity
        # Because we can connect all villages in between with a single wire passing through them
        min_wire = x[last] - x[first]
        results.append(str(min_wire))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()