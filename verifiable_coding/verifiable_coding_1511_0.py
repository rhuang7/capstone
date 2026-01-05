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
        sheet_count = [0] * (N + 2)  # sheet_count[i] is the number of sheets from 0 to i
        for i in range(N):
            if S[i] == ':':
                sheet_count[i+1] = sheet_count[i] + 1
            else:
                sheet_count[i+1] = sheet_count[i]
        
        # Precompute for each pair (i, j) whether it's valid and compute P
        # We'll use a greedy approach to match magnets to irons
        # We'll iterate through each magnet and try to find the closest iron to the left and right that is valid
        
        # First, collect all positions of I and M
        I_pos = []
        M_pos = []
        X_pos = []
        for i in range(N):
            if S[i] == 'I':
                I_pos.append(i)
            elif S[i] == 'M':
                M_pos.append(i)
            elif S[i] == 'X':
                X_pos.append(i)
        
        # Now, for each magnet, try to find an iron to its left and right
        # We'll use a two-pointer approach
        # We'll sort I_pos and M_pos
        I_pos.sort()
        M_pos.sort()
        
        # Now, for each magnet, try to find the closest iron to the left and right that is valid
        # We'll use a pointer for I_pos and M_pos
        i = 0
        j = 0
        count = 0
        
        while i < len(I_pos) and j < len(M_pos):
            # Try to find the closest iron to the left of M_pos[j]
            # We'll move the I pointer forward until we find an iron that is valid
            # We'll check if there is a valid path between M_pos[j] and I_pos[i]
            m = M_pos[j]
            i_pos = I_pos[i]
            
            # Check if there is a block between m and i_pos
            has_block = False
            for x in X_pos:
                if x > min(m, i_pos) and x < max(m, i_pos):
                    has_block = True
                    break
            
            if not has_block:
                # Compute the attraction power
                dist = abs(m - i_pos)
                sheets = sheet_count[max(m, i_pos)] - sheet_count[min(m, i_pos)]
                P = K + 1 - dist - sheets
                if P > 0:
                    count += 1
                    i += 1
                    j += 1
                    continue
            
            # If not valid, move the I pointer forward
            i += 1
        
        results.append(str(count))
    
    print('\n'.join(results))