import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        S = int(data[index])
        SG = int(data[index+1])
        FG = int(data[index+2])
        D = int(data[index+3])
        T_val = int(data[index+4])
        index += 5
        
        # Distance between the cars after T seconds
        distance = D * 50  # in meters
        distance_km = distance / 1000  # convert to km
        
        # Time in hours
        time_h = T_val / 3600
        
        # Speed difference
        speed_diff = distance_km / time_h
        
        # Real speed of other car
        real_speed = S + speed_diff
        
        # Calculate absolute differences
        diff_sebi = abs(real_speed - SG)
        diff_father = abs(real_speed - FG)
        
        if diff_sebi < diff_father:
            results.append("SEBI")
        elif diff_sebi > diff_father:
            results.append("FATHER")
        else:
            results.append("DRAW")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()