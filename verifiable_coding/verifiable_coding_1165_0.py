import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for _ in range(T):
        d = int(data[idx])
        m = data[idx+1]
        idx += 2
        
        month_index = months.index(m)
        day = d
        
        if month_index == 11:  # december
            if day <= 15:
                new_month_index = 0
                new_day = day + 15
            else:
                new_month_index = 1
                new_day = day - 15
        else:
            if day <= 15:
                new_month_index = month_index + 1
                new_day = day + 15
            else:
                new_month_index = month_index
                new_day = day - 15
        
        if new_month_index == 12:
            new_month_index = 0
            new_day = new_day + 15
        
        print(f"{new_day} {months[new_month_index]}")

if __name__ == '__main__':
    solve()