import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+m]))
        idx += m
        
        from collections import defaultdict
        count = defaultdict(int)
        for num in a:
            count[num] += 1
        
        # Convert to powers of two
        power_count = defaultdict(int)
        for num in count:
            power = 0
            while num > 1:
                num >>= 1
                power += 1
            power_count[power] += count[num]
        
        # Try to fill the bag
        res = 0
        current = 0
        for power in range(60, -1, -1):
            needed = (n >> power) & 1
            if needed:
                if power_count[power] > 0:
                    power_count[power] -= 1
                    current += (1 << power)
                else:
                    # Try to split lower powers
                    if power == 0:
                        res = -1
                        break
                    # Split a higher power into two
                    if power_count[power - 1] > 0:
                        power_count[power - 1] += 1
                        res += 1
                    else:
                        res = -1
                        break
            else:
                if power_count[power] > 0:
                    power_count[power] -= 1
                    current += (1 << power)
                else:
                    pass
        results.append(res if res != -1 else -1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()