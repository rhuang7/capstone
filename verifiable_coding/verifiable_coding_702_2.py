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
        # The difference between Th and Tc must be even and divisible by 3
        # Because each minute, the difference reduces by 3 (1 from hot, 2 from cold)
        diff = Th - Tc
        if diff % 3 != 0:
            results.append("Yes")
            continue
        
        # Calculate the number of minutes needed to reach equilibrium
        eq_minutes = diff // 3
        
        if eq_minutes > m:
            results.append("Yes")
        else:
            results.append("No")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()