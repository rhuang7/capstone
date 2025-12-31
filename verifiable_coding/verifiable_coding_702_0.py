import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        m = int(data[index])
        Tc = int(data[index+1])
        Th = int(data[index+2])
        index += 3
        
        # Calculate the time it takes to reach equilibrium
        # The difference between Th and Tc must be even, and the time must be <= m
        diff = Th - Tc
        if diff % 2 != 0:
            # Cannot reach equilibrium, pipe will burst
            results.append("Yes")
            continue
        
        time_to_equilibrium = diff // 2
        
        if time_to_equilibrium <= m:
            # Pipe will not burst
            results.append("No")
        else:
            # Pipe will burst
            results.append("Yes")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()