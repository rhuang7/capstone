import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    results = []
    
    for _ in range(T):
        d = int(data[idx])
        m = data[idx + 1]
        idx += 2
        
        month_idx = months.index(m)
        
        # Find the next month
        next_month_idx = (month_idx + 1) % 12
        
        # If the current month is December, next month is January
        if month_idx == 11:
            next_month_idx = 0
        
        # Calculate the half birthday
        if month_idx == 11:  # December
            # Next month is January, so half birthday is 16th of January
            results.append("16 january")
        else:
            # Calculate the day
            current_day = d
            next_day = month_days[month_idx + 1]
            half_day = (current_day + next_day) // 2
            
            # If the half day is in the next month, adjust
            if current_day > next_day:
                half_day = next_day - (current_day - next_day)
                next_month_idx = (month_idx + 1) % 12
            else:
                half_day = current_day + (next_day - current_day) // 2
                next_month_idx = (month_idx + 1) % 12
            
            results.append(f"{half_day} {months[next_month_idx]}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()