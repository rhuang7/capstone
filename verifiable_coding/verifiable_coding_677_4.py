import sys
import datetime

def solve():
    data = sys.stdin.buffer.read().split()
    day = int(data[0])
    month = int(data[1])
    year = int(data[2])
    date = datetime.date(year, month, day)
    print(date.strftime("%A").capitalize())

if __name__ == '__main__':
    solve()