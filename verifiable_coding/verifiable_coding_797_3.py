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
        
        if s == e:
            possible = []
            for d in range(L, R+1):
                if (d - 1) % 7 == 0:
                    possible.append(d)
            if not possible:
                print("impossible")
            elif len(possible) > 1:
                print("many")
            else:
                print(possible[0])
        else:
            min_days = (e - s + 7) % 7
            possible = []
            for d in range(L, R+1):
                if (d - 1) % 7 == (e - s + 7) % 7:
                    possible.append(d)
            if not possible:
                print("impossible")
            elif len(possible) > 1:
                print("many")
            else:
                print(possible[0])

if __name__ == '__main__':
    solve()