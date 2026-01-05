import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        S = int(data[idx])
        SG = int(data[idx+1])
        FG = int(data[idx+2])
        D = int(data[idx+3])
        T_val = int(data[idx+4])
        idx += 5
        
        # Calculate the distance between the cars after T seconds
        distance = D * 50  # in meters
        distance_km = distance / 1000  # convert to km
        
        # Calculate the relative speed
        time_hours = T_val / 3600
        relative_speed = distance_km / time_hours
        
        # Real speed of the other car
        real_speed = S + relative_speed
        
        # Calculate absolute differences
        diff_sebi = abs(real_speed - SG)
        diff_father = abs(real_speed - FG)
        
        # Determine the result
        if diff_sebi < diff_father:
            results.append("SEBI")
        elif diff_sebi > diff_father:
            results.append("FATHER")
        else:
            results.append("DRAW")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()