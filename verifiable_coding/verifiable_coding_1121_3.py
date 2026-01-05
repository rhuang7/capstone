import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:]
    
    for i in range(T):
        time = cases[i].decode().split(':')
        hours = int(time[0])
        minutes = int(time[1])
        
        # Ensure minutes is a multiple of 5
        minutes = (minutes // 5) * 5
        
        # Calculate positions of hour and minute hands
        minute_angle = 6 * minutes  # 6 degrees per minute
        hour_angle = 30 * hours + 0.5 * minutes  # 30 degrees per hour, 0.5 per minute
        
        # Calculate the absolute difference
        diff = abs(hour_angle - minute_angle)
        
        # The minimum angle is the smaller of diff and 360 - diff
        min_angle = min(diff, 360 - diff)
        
        # Print the result with the correct formatting
        print(f"{min_angle} degree")

if __name__ == '__main__':
    solve()