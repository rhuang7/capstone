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
        
        # Preprocess the string to track positions of I, M, X, and count of :
        I_pos = []
        M_pos = []
        X_pos = []
        sheet_count = [0] * (N + 2)  # 1-based indexing
        sheet_count[0] = 0
        sheet_count[N+1] = 0
        
        for i in range(N):
            if S[i] == 'I':
                I_pos.append(i)
            elif S[i] == 'M':
                M_pos.append(i)
            elif S[i] == 'X':
                X_pos.append(i)
            elif S[i] == ':':
                sheet_count[i+1] = sheet_count[i] + 1
        
        # For each M, find all I that can be attracted
        max_magnets = 0
        for m in M_pos:
            for i in I_pos:
                # Check if there is a block between m and i
                has_block = False
                for x in X_pos:
                    if x > m and x < i:
                        has_block = True
                        break
                if has_block:
                    continue
                
                # Calculate the attraction power
                dist = abs(i - m)
                sheets = sheet_count[i+1] - sheet_count[m]
                P = K + 1 - dist - sheets
                if P > 0:
                    max_magnets += 1
                    break  # Each I can be assigned to at most one M
        
        results.append(str(max_magnets))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()