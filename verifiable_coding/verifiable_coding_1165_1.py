import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    month_indices = {month: i for i, month in enumerate(months)}
    
    results = []
    for _ in range(T):
        d = int(data[idx])
        m = data[idx+1]
        idx += 2
        
        month_idx = month_indices[m]
        next_month = (month_idx + 1) % 12
        next_month_name = months[next_month]
        
        if month_idx == 1:  # february
            if d <= 28:
                if next_month == 1:  # next is february again (leap year)
                    d1 = d + 14
                else:
                    d1 = d + 14
            else:
                if next_month == 1:  # next is february again (leap year)
                    d1 = d - 14
                else:
                    d1 = d - 14
        else:
            if d <= 30:
                if next_month == 1:  # next is february again (leap year)
                    d1 = d + 14
                else:
                    d1 = d + 14
            else:
                if next_month == 1:  # next is february again (leap year)
                    d1 = d - 14
                else:
                    d1 = d - 14
        
        results.append(f"{d1} {next_month_name}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()