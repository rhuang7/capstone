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
        
        # Calculate the equilibrium temperature
        # Let equilibrium be Te
        # After some steps, the temperatures will converge to Te
        # Let's find the equilibrium temperature
        # Let's assume that the process can reach equilibrium in some steps
        # Let's find the equilibrium temperature
        
        # The difference between Th and Tc is D = Th - Tc
        # Each minute, the larger temperature decreases by 1, and the smaller increases by 2
        # So the net change per minute is -1 + 2 = +1 for the difference
        # So the difference decreases by 1 per minute
        # So the time to reach equilibrium is D minutes
        # But if m >= D, then equilibrium is reached
        # If m < D, then the difference is D - m
        # If the difference is not zero after m minutes, then the pipe will burst
        
        D = Th - Tc
        if m >= D:
            results.append("No")
        else:
            # After m minutes, the difference is D - m
            # The pipe will burst if the difference is not zero
            if (D - m) % 3 != 0:
                results.append("Yes")
            else:
                results.append("No")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()