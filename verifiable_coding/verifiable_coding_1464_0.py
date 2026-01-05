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
    if month < 3:
        year -= 1
        month += 12
    if month == 1:
        return day
    elif month == 2:
        return 31 + day
    elif month == 3:
        return 59 + day
    elif month == 4:
        return 90 + day
    elif month == 5:
        return 120 + day
    elif month == 6:
        return 151 + day
    elif month == 7:
        return 181 + day
    elif month == 8:
        return 212 + day
    elif month == 9:
        return 243 + day
    elif month == 10:
        return 273 + day
    elif month == 11:
        return 304 + day
    else:  # month == 12
        return 334 + day

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for case in cases:
        y, m, d = map(int, case.split(':'))
        initial_day = d
        count = 1
        current_day = initial_day
        current_year = y
        current_month = m
        current_day = d
        
        while True:
            next_day = current_day + 2
            if next_day > 31:
                if current_month == 12:
                    current_month = 1
                    current_year += 1
                else:
                    current_month += 1
                next_day = 1
            if next_day % 2 == initial_day % 2:
                count += 1
                current_day = next_day
            else:
                break
        print(count)

if __name__ == '__main__':
    solve()