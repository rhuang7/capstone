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
        
        # Days needed for high quality
        high_days = full_cycles * g + remainder
        
        # Total days needed is high_days + (full_cycles * b)
        total_days = high_days + full_cycles * b
        
        # But we also need to make sure that we have enough days to complete the entire highway
        # So we take the maximum between total_days and n
        results.append(max(total_days, n))
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()