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
        # Find positions of villages without electricity
        no_electricity = [i for i in range(n) if s[i] == '0']
        
        # If no villages without electricity, no wire needed
        if not no_electricity:
            results.append(0)
            continue
        
        # Connect the villages without electricity to the nearest available electricity
        # We can connect all no_electricity villages to the nearest electricity in a way that minimizes total distance
        # We can use a two-pointer approach to connect the no_electricity villages to the electricity villages
        # Start from the leftmost no_electricity village and the leftmost electricity village
        # Move the pointer that is at the smaller position
        i = 0  # pointer for no_electricity
        j = 0  # pointer for has_electricity
        total = 0
        
        while i < len(no_electricity) and j < len(has_electricity):
            if x[no_electricity[i]] < x[has_electricity[j]]:
                # Connect this no_electricity village to the next electricity village
                total += x[has_electricity[j]] - x[no_electricity[i]]
                i += 1
            else:
                # Connect this electricity village to the next no_electricity village
                total += x[no_electricity[i]] - x[has_electricity[j]]
                j += 1
        
        # If there are still no_electricity villages left, connect them to the last electricity village
        while i < len(no_electricity):
            total += x[has_electricity[-1]] - x[no_electricity[i]]
            i += 1
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()