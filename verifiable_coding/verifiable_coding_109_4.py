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
        
        # Convert counts to log2 for easier handling
        log_count = {}
        for power in count:
            log_count[power] = count[power]
        
        # We need to find the minimum number of divisions
        # to get the required sum of powers of two
        # Start from the highest power of two less than or equal to n
        # and work downwards
        required = n
        divisions = 0
        
        # Find the highest power of two less than or equal to n
        max_power = 1
        while max_power <= n:
            max_power <<= 1
        max_power >>= 1
        
        # Try to fill the bag starting from the highest power
        while required > 0:
            # Check if we have the current power
            if max_power in log_count:
                log_count[max_power] -= 1
                if log_count[max_power] == 0:
                    del log_count[max_power]
                required -= max_power
                continue
            # If not, try to split the next higher power
            if max_power * 2 in log_count:
                # Split the higher power into two
                log_count[max_power * 2] -= 1
                if log_count[max_power * 2] == 0:
                    del log_count[max_power * 2]
                log_count[max_power] += 2
                divisions += 1
                max_power <<= 1
            else:
                # No power available, impossible
                results.append(-1)
                break
        else:
            # If we exited the loop normally, required is 0
            results.append(divisions)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()