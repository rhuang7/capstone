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
        
        distance = D * 50  # meters
        distance_km = distance / 1000  # convert to km
        
        # Calculate the relative distance covered in T seconds
        # Convert S to m/s
        S_mps = S * 1000 / 3600
        # Distance covered by Sebi's car in T seconds
        dist_sebi = S_mps * T_val
        
        # The other car is faster, so its distance is dist_sebi + distance_km
        # Convert to m/s
        other_speed_mps = (dist_sebi + distance_km) / T_val
        
        # Convert to kph
        other_speed_kph = other_speed_mps * 3600 / 1000
        
        # Calculate absolute differences
        diff_sebi = abs(other_speed_kph - SG)
        diff_father = abs(other_speed_kph - FG)
        
        if diff_sebi < diff_father:
            results.append("SEBI")
        elif diff_father < diff_sebi:
            results.append("FATHER")
        else:
            results.append("DRAW")
    
    print('\n'.join(results))