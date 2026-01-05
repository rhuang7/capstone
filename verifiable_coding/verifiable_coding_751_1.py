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
        electrified = []
        for i in range(n):
            if s[i] == '1':
                electrified.append(x[i])
        
        # Find the closest electrified village to each un-electrified village
        # and calculate the total wire length
        total = 0
        prev = None
        for i in range(n):
            if s[i] == '0':
                if prev is None:
                    # No electrified village before, take the first one
                    total += abs(x[i] - electrified[0])
                else:
                    # Find the closest electrified village
                    # Binary search for the insertion point
                    pos = bisect.bisect_left(electrified, x[i])
                    if pos == 0:
                        total += abs(x[i] - electrified[0])
                    elif pos == len(electrified):
                        total += abs(x[i] - electrified[-1])
                    else:
                        total += min(abs(x[i] - electrified[pos]), abs(x[i] - electrified[pos - 1]))
            else:
                prev = x[i]
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()