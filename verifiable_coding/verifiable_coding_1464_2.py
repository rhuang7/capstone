import sys
import datetime

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    else:
        return year % 400 == 0

def get_next_date(year, month, day):
    if month == 12 and day == 31:
        return (year + 1, 1, 1)
    elif month == 12 and day == 30:
        return (year, 1, 1)
    elif month == 12 and day == 31:
        return (year + 1, 1, 1)
    elif month == 2:
        if is_leap(year):
            if day == 29:
                return (year, 3, 1)
            else:
                return (year, 2, day + 1)
        else:
            if day == 28:
                return (year, 3, 1)
            else:
                return (year, 2, day + 1)
    else:
        if month in [4, 6, 9, 11]:
            if day == 30:
                return (year, month + 1, 1)
            else:
                return (year, month, day + 1)
        else:
            if day == 31:
                return (year, month + 1, 1)
            else:
                return (year, month, day + 1)

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for case in cases:
        year, month, day = map(int, case.split(':'))
        current_day = datetime.date(year, month, day)
        next_day = current_day + datetime.timedelta(days=2)
        count = 1
        while True:
            current_day = datetime.date(year, month, day)
            next_day = current_day + datetime.timedelta(days=2)
            if next_day.day % 2 == current_day.day % 2:
                count += 1
            else:
                break
        print(count)

if __name__ == '__main__':
    solve()