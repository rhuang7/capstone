import sys
import calendar

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:]
    
    for i in range(T):
        date_str = cases[i].decode('utf-8')
        year, month, day = map(int, date_str.split(':'))
        is_odd = day % 2 == 1
        
        count = 1
        current_day = day
        current_month = month
        current_year = year
        
        while True:
            current_day += 1
            if current_day > days_in_month(current_year, current_month):
                current_month += 1
                if current_month > 12:
                    current_year += 1
                    current_month = 1
                current_day = 1
            if (current_day % 2 == 1 and is_odd) or (current_day % 2 == 0 and not is_odd):
                count += 1
            else:
                break
        print(count)

if __name__ == '__main__':
    solve()