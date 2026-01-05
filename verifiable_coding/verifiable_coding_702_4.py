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
        # The difference between Th and Tc must be even
        diff = Th - Tc
        if diff % 2 != 0:
            results.append("Yes")
            continue
        
        # Time to reach equilibrium
        time_to_eq = diff // 2
        
        if time_to_eq <= m:
            results.append("Yes")
        else:
            results.append("No")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()