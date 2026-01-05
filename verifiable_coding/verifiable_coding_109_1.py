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
        
        # Convert counts to log2 values
        log_counts = {}
        for power in count:
            log_counts[power] = count[power]
        
        # We need to find the minimum number of divisions to reach exactly n
        # We'll use a greedy approach starting from the largest power of two less than or equal to n
        # and work our way down
        
        # Find the maximum power of two less than or equal to n
        max_power = 0
        while (1 << (max_power + 1)) <= n:
            max_power += 1
        
        res = 0
        current = n
        while current > 0:
            # Find the largest power of two <= current
            power = 0
            while (1 << (power + 1)) <= current:
                power += 1
            size = 1 << power
            
            # Check if we have this size
            if size in log_counts:
                log_counts[size] -= 1
                if log_counts[size] == 0:
                    del log_counts[size]
                current -= size
                continue
            # If not, try to split a larger size
            if size * 2 in log_counts:
                # Split the size * 2 into two size
                log_counts[size * 2] -= 1
                if log_counts[size * 2] == 0:
                    del log_counts[size * 2]
                log_counts[size] += 2
                res += 1
                # Now try again with the new size
                current = n
                continue
            # If neither, it's impossible
            results.append(-1)
            break
        else:
            results.append(res)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()