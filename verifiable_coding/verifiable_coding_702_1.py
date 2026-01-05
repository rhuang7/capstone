import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        m = int(data[idx])
        Tc = int(data[idx+1])
        Th = int(data[idx+2])
        idx += 3
        
        # Calculate the time it takes to reach equilibrium
        # The difference between Th and Tc is D = Th - Tc
        # Each minute, the difference decreases by 3 (1 from the hotter, 2 from the colder)
        D = Th - Tc
        if D == 0:
            # Already in equilibrium
            results.append("No")
            continue
        # Time to reach equilibrium
        time_to_eq = (D + 2) // 3  # Ceiling division
        
        if time_to_eq > m:
            # Pipe will burst because it hasn't reached equilibrium in m minutes
            results.append("Yes")
        else:
            # Pipe will not burst
            results.append("No")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()