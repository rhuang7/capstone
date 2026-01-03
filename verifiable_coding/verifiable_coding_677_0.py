import sys
import calendar

def solve():
    data = sys.stdin.buffer.read().split()
    day = int(data[0])
    month = int(data[1])
    year = int(data[2])
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    total_days = sum(days_in_month[:month-1]) + day
    day_of_week = total_days % 7
    if day_of_week == 0:
        print("Sunday")
    elif day_of_week == 1:
        print("Monday")
    elif day_of_week == 2:
        print("Tuesday")
    elif day_of_week == 3:
        print("Wednesday")
    elif day_of_week == 4:
        print("Thursday")
    elif day_of_week == 5:
        print("Friday")
    else:
        print("Saturday")

if __name__ == '__main__':
    solve()