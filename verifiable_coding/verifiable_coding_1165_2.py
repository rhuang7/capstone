import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    
    for _ in range(T):
        d = int(data[index])
        m = data[index + 1]
        index += 2
        
        month_index = months.index(m)
        
        # Find the next month
        next_month_index = (month_index + 1) % 12
        
        # Find the number of days in the current month
        if month_index == 1:  # february
            days = 29
        elif month_index in [3, 5, 8, 10]:  # april, june, september, november
            days = 30
        else:
            days = 31
        
        # Calculate the half birthday
        if d <= days // 2:
            d1 = d + days // 2
            m1 = months[month_index]
        else:
            d1 = d - days // 2
            m1 = months[next_month_index]
        
        print(f"{d1} {m1}")

if __name__ == '__main__':
    solve()