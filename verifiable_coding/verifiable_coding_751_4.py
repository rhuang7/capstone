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
        if not has_electricity:
            results.append(0)
            continue
        
        # Find the first and last village with electricity
        first = has_electricity[0]
        last = has_electricity[-1]
        
        # The minimum wire length is the distance between the first and last village with electricity
        # Because we can connect all villages without electricity in between by connecting to the first and last
        min_wire = x[last] - x[first]
        results.append(min_wire)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()