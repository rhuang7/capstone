import sys
import calendar

def solve():
    data = sys.stdin.buffer.read().split()
    day = int(data[0])
    month = int(data[1])
    year = int(data[2])
    
    # Get the weekday (0 is Monday, 1 is Tuesday, ..., 6 is Sunday)
    weekday = calendar.weekday(year, month, day)
    
    # Map weekday to day name
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(days[weekday])

if __name__ == '__main__':
    solve()