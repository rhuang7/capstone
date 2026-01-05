import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        m = int(data[index])
        d = int(data[index+1])
        w = int(data[index+2])
        index += 3
        
        # Calculate the total number of days in the year
        total_days = m * d
        
        # Calculate the number of days in the week
        week_days = w
        
        # Calculate the number of days in the year modulo week_days
        mod = total_days % week_days
        
        # If mod is 0, then the year ends on a day that is the same as the first day
        # So the last day of the year is the same as the first day of the week
        # This affects the number of ambiguous pairs
        if mod == 0:
            # The last day of the year is the same as the first day of the week
            # So the last day of the year is the same as the first day of the week
            # So the pair (d, m) is ambiguous
            # But since x < y, we need to check if d < m
            if d < m:
                results.append(1)
            else:
                results.append(0)
        else:
            # The last day of the year is not the same as the first day of the week
            # So no additional pair is added
            results.append(0)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()