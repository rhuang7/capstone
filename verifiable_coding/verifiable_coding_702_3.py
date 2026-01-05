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
        
        # Calculate the time needed to reach equilibrium
        # The difference between Th and Tc is D
        D = Th - Tc
        # Each minute, the difference decreases by 3 (1 from hot, 2 from cold)
        # So time to equilibrium is D // 3
        time_to_eq = D // 3
        
        if time_to_eq > m:
            results.append("Yes")
        else:
            # Check if after m minutes, the temperatures are still not equal
            # After m minutes, the difference is D - 3 * m
            # If D - 3 * m != 0, then it's not equilibrium
            if (Th - Tc) % 3 != 0:
                results.append("Yes")
            else:
                results.append("No")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()