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
        
        # Function to calculate days to reach Z
        def days_to_reach(target, current, increment):
            if current >= target:
                return 0
            return (target - current + increment - 1) // increment
        
        # Calculate days for each company to reach Z
        days_pied = days_to_reach(Z, A, X)
        days_hooli = days_to_reach(Z, B, Y)
        
        # If Hooli reaches first or same day, output RIP
        if days_hooli <= days_pied:
            results.append("RIP")
            continue
        
        # Otherwise, find minimum contributions
        # Sort contributions in descending order
        C.sort(reverse=True)
        contributions = 0
        current_pied = A
        current_hooli = B
        
        # Try to contribute until either company reaches Z
        while True:
            # Check if current_pied or current_hooli has reached Z
            if current_pied >= Z or current_hooli >= Z:
                break
            # Try to contribute the largest available contribution
            if C:
                contribution = C[0]
                # If contribution is 0, skip
                if contribution == 0:
                    break
                # Add contribution to Pied Piper
                current_pied += contribution
                contributions += 1
                # Halve the contribution
                C[0] = C[0] // 2
                # Re-sort the list
                C.sort(reverse=True)
            else:
                break
        
        results.append(str(contributions))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()