import sys
import datetime

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    else:
        return year % 400 == 0

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
    cases = input[1:T+1]
    
    for case in cases:
        y, m, d = map(int, case.split(':'))
        start_date = datetime.date(y, m, d)
        current_date = start_date
        count = 1
        while True:
            next_date = current_date + datetime.timedelta(days=2)
            if next_date.day % 2 == d % 2:
                count += 1
                current_date = next_date
            else:
                break
        print(count)

if __name__ == '__main__':
    solve()