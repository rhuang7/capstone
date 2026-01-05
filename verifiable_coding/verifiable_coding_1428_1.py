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
        
        # Calculate days until each company reaches Z
        def days_to_reach_z(current, daily_gain, target):
            if current >= target:
                return 0
            return (target - current + daily_gain - 1) // daily_gain
        
        days_pied = days_to_reach_z(A, X, Z)
        days_hooli = days_to_reach_z(B, Y, Z)
        
        if days_hooli <= days_pied:
            results.append("RIP")
            continue
        
        # Now find the minimum number of contributions needed
        # Sort supporters in descending order of contribution value
        C.sort(reverse=True)
        contributions = 0
        current_users = A
        
        for c in C:
            if current_users >= Z:
                break
            # Add contribution
            current_users += c
            contributions += 1
            # Halve the contribution
            c = c // 2
        
        # Check if even after all contributions, Pied Piper can reach Z
        if current_users < Z:
            results.append("RIP")
        else:
            results.append(str(contributions))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()