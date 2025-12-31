import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        n = int(data[index])
        g = int(data[index+1])
        b = int(data[index+2])
        index += 3
        
        required_high = (n + 1) // 2
        
        # Calculate how many good days are needed to reach required_high
        # Each good day can contribute 1 to high quality
        # Each cycle is g + b days
        full_cycles = required_high // g
        remainder = required_high % g
        
        # Total days needed for high quality
        high_days = full_cycles * (g + b) + remainder
        
        # Total days needed for the whole highway
        # We need to repair n units, so we need at least n days
        # But we can do it in high_days days if high_days >= n
        # Otherwise, we need to repair the remaining units in the next days
        if high_days >= n:
            results.append(high_days)
        else:
            # We need to repair the remaining (n - high_days) units
            # These can be done in the next (n - high_days) days
            # But we have to make sure that we have enough days
            # The total days is high_days + (n - high_days) = n
            results.append(n)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()