import sys
import calendar

def solve():
    data = sys.stdin.buffer.read().split()
    day = int(data[0])
    month = int(data[1])
    year = int(data[2])
    day_of_week = calendar.weekday(year, month, day)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(days[day_of_week])

if __name__ == '__main__':
    solve()