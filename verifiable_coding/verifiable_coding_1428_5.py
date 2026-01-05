import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        A = int(data[idx+1])
        B = int(data[idx+2])
        X = int(data[idx+3])
        Y = int(data[idx+4])
        Z = int(data[idx+5])
        idx += 6
        C = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Check if Pied Piper can already take over
        if A >= Z:
            results.append("RIP")
            continue
        # Check if Hooli will always take over
        days_pied = (Z - A + X - 1) // X
        days_hooli = (Z - B + Y - 1) // Y
        if days_hooli <= days_pied:
            results.append("RIP")
            continue
        
        # Now find the minimum contributions
        # Sort contributions in descending order
        C.sort(reverse=True)
        contributions = 0
        current_A = A
        current_B = B
        
        for c in C:
            # Check if we can take over before this contribution
            days_pied = (Z - current_A + X - 1) // X
            days_hooli = (Z - current_B + Y - 1) // Y
            if days_hooli <= days_pied:
                break
            # Contribute
            current_A += c
            contributions += 1
            # Halve the contribution
            c = c // 2
        
        # Check if we can take over after all contributions
        days_pied = (Z - current_A + X - 1) // X
        days_hooli = (Z - current_B + Y - 1) // Y
        if days_hooli <= days_pied:
            results.append("RIP")
        else:
            results.append(str(contributions))
    
    print('\n'.join(results))