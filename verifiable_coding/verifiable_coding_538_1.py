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
        
        # Calculate distance between the cars after T seconds
        distance = D * 50  # in meters
        distance_km = distance / 1000  # convert to km
        
        # Time in hours
        time_h = T_val / 3600
        
        # Speed difference
        speed_diff = (distance_km) / time_h
        
        # Real speed of other car
        real_speed = S + speed_diff
        
        # Calculate absolute differences
        diff_sebi = abs(real_speed - SG)
        diff_father = abs(real_speed - FG)
        
        # Determine result
        if diff_sebi < diff_father:
            results.append("SEBI")
        elif diff_father < diff_sebi:
            results.append("FATHER")
        else:
            results.append("DRAW")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()