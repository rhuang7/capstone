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
        # Equilibrium is when the temperatures are equal
        # Let's find how many steps it takes to reach equilibrium
        # Let's assume Th >= Tc
        # Let's find the number of steps to reach equilibrium
        
        # Let's find the difference
        diff = Th - Tc
        
        # Each step, the larger temperature decreases by 1, the smaller increases by 2
        # So, the difference decreases by 3 per step
        # So, the number of steps to equilibrium is (diff + 2) // 3
        steps_to_eq = (diff + 2) // 3
        
        if steps_to_eq > m:
            # Pipe will burst because it hasn't reached equilibrium in m minutes
            results.append("Yes")
        else:
            # Pipe will not burst
            results.append("No")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()