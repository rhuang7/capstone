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
        
        # Convert counts to powers of two
        power_counts = {}
        for power in count:
            exp = 0
            while power > 1:
                power >>= 1
                exp += 1
            power_counts[exp] = count[power]
        
        # Try to fill the bag starting from the highest power
        res = 0
        for exp in range(60, -1, -1):
            if n >= (1 << exp):
                needed = (n >> exp) & 1
                if needed:
                    if power_counts.get(exp, 0) > 0:
                        power_counts[exp] -= 1
                        n -= (1 << exp)
                        res += 0
                    else:
                        # Try to split lower powers
                        for i in range(exp-1, -1, -1):
                            if power_counts.get(i, 0) > 0:
                                power_counts[i] -= 1
                                res += 1
                                n -= (1 << i)
                                if n == 0:
                                    break
                        if n != 0:
                            results.append(-1)
                            break
                else:
                    continue
            else:
                continue
        else:
            if n == 0:
                results.append(res)
            else:
                results.append(-1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()