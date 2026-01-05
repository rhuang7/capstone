import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        time = data[i].decode()
        hours, minutes = map(int, time.split(':'))
        
        # Calculate minute hand angle
        minute_angle = 6 * minutes  # 6 degrees per minute
        
        # Calculate hour hand angle
        hour_angle = 30 * hours + 0.5 * minutes  # 30 degrees per hour, 0.5 degrees per minute
        
        # Calculate the absolute difference
        diff = abs(hour_angle - minute_angle)
        
        # Minimum angle is the smaller of diff and 360 - diff
        min_angle = min(diff, 360 - diff)
        
        results.append(f"{int(min_angle)} degree")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()