import sys

def solve():
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day_index = {day: i for i, day in enumerate(days)}
    
    T = int(sys.stdin.buffer.read().split()[0])
    data = sys.stdin.buffer.read().split()
    
    idx = 0
    for _ in range(T):
        S = data[idx]
        E = data[idx+1]
        L = int(data[idx+2])
        R = int(data[idx+3])
        idx += 4
        
        s = day_index[S]
        e = day_index[E]
        
        # Calculate the minimum and maximum possible durations
        min_days = (e - s + 7) % 7
        max_days = (e - s + 7) % 7
        
        # Find all durations in [L, R] that satisfy the condition
        possible = []
        for d in range(L, R+1):
            if (e - s + 7) % 7 == (d - 1) % 7:
                possible.append(d)
        
        if len(possible) == 0:
            print("impossible")
        elif len(possible) > 1:
            print("many")
        else:
            print(possible[0])

if __name__ == '__main__':
    solve()