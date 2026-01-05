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
        
        # Convert to log2 for easier handling
        log_counts = {}
        for power in count:
            log = power.bit_length() - 1
            log_counts[log] = count[power]
        
        # We need to find the minimum number of divisions to get enough boxes of each power
        # to sum up to n
        # We'll try to fill from the highest power down to the lowest
        # We'll keep track of how much we have and how much we need
        
        # Initialize the current sum
        current_sum = 0
        divisions = 0
        
        # We'll process from the highest possible power down to 0
        max_power = 60  # since 2^60 is larger than 1e18
        for power in range(max_power, -1, -1):
            needed = (n - current_sum) // (1 << power)
            if needed <= 0:
                continue
            # We need to get 'needed' boxes of this power
            # We can get from existing boxes or by dividing larger boxes
            # First try to use existing boxes
            have = log_counts.get(power, 0)
            if have >= needed:
                current_sum += needed * (1 << power)
                continue
            # We need more boxes of this power
            # We can get them by dividing larger boxes
            # So we need to find boxes of higher power and divide them
            # We'll go to the next higher power
            higher_power = power + 1
            while higher_power <= max_power:
                if log_counts.get(higher_power, 0) > 0:
                    # We can divide one box of higher_power into two of power+1
                    # Then we can divide those into two of power
                    # So each box of higher_power can contribute 2^(higher_power - power) boxes of power
                    # We need to find how many boxes of higher_power we need to get at least 'needed' boxes of power
                    # The number of boxes needed is ceil(needed / 2^(higher_power - power))
                    required_boxes = (needed + (1 << (higher_power - power)) - 1) // (1 << (higher_power - power))
                    if log_counts.get(higher_power, 0) >= required_boxes:
                        # We can take 'required_boxes' boxes of higher_power
                        # Each contributes 2^(higher_power - power) boxes of power
                        current_sum += required_boxes * (1 << (higher_power - power)) * (1 << power)
                        divisions += required_boxes * (higher_power - power)
                        # Remove those boxes from log_counts
                        log_counts[higher_power] -= required_boxes
                        if log_counts[higher_power] == 0:
                            del log_counts[higher_power]
                        break
                    else:
                        # Not enough boxes of higher_power, try next higher power
                        higher_power += 1
                else:
                    higher_power += 1
            else:
                # No higher power found to get the needed boxes
                results.append(-1)
                break
        else:
            # If we've processed all powers and current_sum >= n
            if current_sum >= n:
                results.append(divisions)
            else:
                results.append(-1)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()