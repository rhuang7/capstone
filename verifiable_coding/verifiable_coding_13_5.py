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
        
        # Calculate how many full cycles of (g + b) days are needed
        full_cycles = required_high // (g + b)
        remainder = required_high % (g + b)
        
        # Days needed for full cycles
        days = full_cycles * (g + b)
        
        # Days needed for remainder
        # If remainder <= g, we can do it in remainder days
        # Else, we need g days for high quality + (remainder - g) days for low quality
        if remainder <= g:
            days += remainder
        else:
            days += g + (remainder - g)
        
        results.append(days)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()