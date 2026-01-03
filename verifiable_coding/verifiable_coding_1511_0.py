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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        S = data[idx]
        idx += 1
        
        # Preprocess: record positions of I, M, X, and count sheets
        I_pos = []
        M_pos = []
        X_pos = []
        sheet_count = [0] * (N + 2)  # 1-based to N
        
        for i in range(N):
            if S[i] == 'I':
                I_pos.append(i)
            elif S[i] == 'M':
                M_pos.append(i)
            elif S[i] == 'X':
                X_pos.append(i)
            elif S[i] == ':':
                sheet_count[i+1] += 1
        
        # Precompute prefix sums of sheets
        prefix_sheets = [0] * (N + 2)
        for i in range(1, N+1):
            prefix_sheets[i] = prefix_sheets[i-1] + sheet_count[i]
        
        # For each magnet, find possible iron pieces it can attract
        # and count the maximum matching
        # Use a greedy approach: for each magnet, try to match with the closest possible iron
        # that is not yet matched and satisfies the condition
        
        matched = [False] * N
        count = 0
        
        for m in M_pos:
            for i in I_pos:
                if i == m or matched[i]:
                    continue
                # Check if there are no X between m and i
                has_x = False
                for j in range(min(m, i)+1, max(m, i)):
                    if S[j] == 'X':
                        has_x = True
                        break
                if has_x:
                    continue
                # Compute distance and number of sheets between m and i
                dist = abs(m - i)
                sheets = prefix_sheets[max(m, i)] - prefix_sheets[min(m, i)]
                power = K + 1 - dist - sheets
                if power > 0:
                    matched[i] = True
                    count += 1
                    break
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()