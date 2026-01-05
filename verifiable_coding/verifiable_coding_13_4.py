import sys

def solve():
    import math
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
        
        required_high_quality = (n + 1) // 2
        
        # Calculate how many good days are needed
        good_days_needed = required_high_quality
        
        # Calculate the number of full cycles of (g + b) days
        full_cycles = good_days_needed // g
        remainder = good_days_needed % g
        
        # Total days needed
        total_days = full_cycles * (g + b) + remainder
        
        # If total_days is less than n, we need to add the remaining days
        if total_days < n:
            total_days = n
        
        results.append(total_days)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()