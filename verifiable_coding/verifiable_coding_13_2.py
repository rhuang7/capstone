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
        
        # Calculate how many full cycles of (g + b) days are needed
        full_cycles = required_high_quality // g
        remainder = required_high_quality % g
        
        # Days needed for full cycles
        days = full_cycles * (g + b)
        
        # Add days for the remainder
        days += remainder
        
        # If the total days is less than n, we need to add the remaining days
        if days < n:
            days = n
        
        results.append(days)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()