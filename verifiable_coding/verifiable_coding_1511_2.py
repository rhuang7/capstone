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
        
        # Preprocess: track positions of I, M, X, and count sheets
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
        
        # For each magnet, find possible irons it can attract
        # We'll use a greedy approach: match magnets to irons as soon as possible
        matched = [False] * N
        count = 0
        
        for m in M_pos:
            for i in I_pos:
                if i < m:
                    continue
                # Check if there's a block between m and i
                has_block = False
                for x in X_pos:
                    if x > m and x < i:
                        has_block = True
                        break
                if has_block:
                    continue
                # Compute attraction power
                dist = i - m
                sheets = prefix_sheets[i] - prefix_sheets[m]
                power = K + 1 - dist - sheets
                if power > 0:
                    if not matched[i]:
                        matched[i] = True
                        count += 1
                        break  # Move to next magnet
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()