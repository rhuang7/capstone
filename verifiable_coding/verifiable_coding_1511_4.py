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
        # We'll use a greedy approach: match magnets to iron pieces as soon as possible
        matched = [False] * N
        count = 0
        
        for m in M_pos:
            for i in range(len(I_pos)):
                if matched[I_pos[i]]:
                    continue
                iron = I_pos[i]
                if iron in X_pos:
                    continue
                # Check if there's a block between m and iron
                has_block = False
                for x in X_pos:
                    if m < x < iron or iron < x < m:
                        has_block = True
                        break
                if has_block:
                    continue
                # Calculate attraction power
                dist = abs(iron - m)
                sheets = prefix_sheets[iron] - prefix_sheets[m]
                power = K + 1 - dist - sheets
                if power > 0:
                    count += 1
                    matched[iron] = True
                    break
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()