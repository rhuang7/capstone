import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    results = []
    
    for _ in range(T):
        d = int(data[idx])
        m = data[idx+1]
        idx += 2
        
        month_index = months.index(m)
        day = d
        
        if month_index == 11:  # december
            if day <= 15:
                results.append(f"{day + 15} january")
            else:
                results.append(f"{day - 15} january")
        else:
            if day <= (month_days[month_index] // 2):
                results.append(f"{day + (month_days[month_index] // 2)} {months[month_index]}")
            else:
                results.append(f"{day - (month_days[month_index] // 2)} {months[month_index + 1]}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()