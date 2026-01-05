import sys
import datetime

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    else:
        return year % 400 == 0

def get_day_of_year(year, month, day):
    dt = datetime.date(year, month, day)
    return dt.timetuple().tm_yday

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for case in cases:
        y, m, d = map(int, case.split(':'))
        initial_day = d
        correct_day = initial_day
        count = 1
        current_year = y
        current_month = m
        current_day = d
        
        while True:
            # Move to next day
            current_day += 1
            if current_day > 31:
                current_month += 1
                current_day = 1
                if current_month > 12:
                    current_year += 1
                    current_month = 1
                    current_day = 1
            
            # Check if next day is leap year
            is_leap_year = is_leap(current_year)
            
            # Check if next day is valid
            if current_month in [4, 6, 9, 11] and current_day > 30:
                current_month += 1
                current_day = 1
                if current_month > 12:
                    current_year += 1
                    current_month = 1
                    current_day = 1
            elif current_month == 2 and is_leap_year and current_day > 29:
                current_month += 1
                current_day = 1
                if current_month > 12:
                    current_year += 1
                    current_month = 1
                    current_day = 1
            elif current_month == 2 and not is_leap_year and current_day > 28:
                current_month += 1
                current_day = 1
                if current_month > 12:
                    current_year += 1
                    current_month = 1
                    current_day = 1
            
            # Check if next day is correct
            next_day = current_day
            if next_day % 2 == 0:
                if initial_day % 2 == 0:
                    count += 1
                else:
                    print(count)
                    break
            else:
                if initial_day % 2 == 1:
                    count += 1
                else:
                    print(count)
                    break

if __name__ == '__main__':
    solve()