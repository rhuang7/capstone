import sys
import datetime

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    else:
        return year % 400 == 0

def get_next_date(date_str):
    year, month, day = map(int, date_str.split(':'))
    date = datetime.date(year, month, day)
    next_date = date + datetime.timedelta(days=1)
    return next_date.strftime("%Y:%m:%d")

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for case in cases:
        date_str = case.decode('utf-8')
        year, month, day = map(int, date_str.split(':'))
        date = datetime.date(year, month, day)
        next_date = date + datetime.timedelta(days=1)
        next_date_str = next_date.strftime("%Y:%m:%d")
        
        # Check if next date is even or odd
        day = int(date_str.split(':')[2])
        if day % 2 == 0:
            # Should take pill on even days
            if int(next_date_str.split(':')[2]) % 2 != 0:
                print(1)
            else:
                print(2)
        else:
            # Should take pill on odd days
            if int(next_date_str.split(':')[2]) % 2 != 1:
                print(1)
            else:
                print(2)

if __name__ == '__main__':
    solve()