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
        
        # Preprocess the string to store positions of I, M, X, and count of :
        I_pos = []
        M_pos = []
        X_pos = []
        sheet_count = [0] * (N + 2)  # sheet_count[i] is the number of : between i and i+1
        for i in range(N-1):
            if S[i] == ':':
                sheet_count[i+1] += 1
            if S[i+1] == ':':
                sheet_count[i+1] += 1
        
        # Precompute for each M, the possible I's it can attract
        # We'll use a greedy approach: for each I, assign the closest possible M that hasn't been assigned yet
        # We'll use a list to track which M's are used
        used_m = [False] * len(M_pos)
        count = 0
        
        # Iterate through each I
        for i in range(N):
            if S[i] == 'I':
                # Find the closest M to the left that hasn't been used and is valid
                for j in range(len(M_pos)-1, -1, -1):
                    m = M_pos[j]
                    if m >= i:
                        continue
                    # Check if there's a blocked cell between m and i
                    blocked = False
                    for k in range(m+1, i):
                        if S[k] == 'X':
                            blocked = True
                            break
                    if blocked:
                        continue
                    # Calculate the attraction power
                    dist = i - m
                    sheets = sheet_count[m+1] + sheet_count[i]
                    power = K + 1 - dist - sheets
                    if power > 0:
                        used_m[j] = True
                        count += 1
                        break
                # Find the closest M to the right that hasn't been used and is valid
                for j in range(len(M_pos)):
                    m = M_pos[j]
                    if m <= i:
                        continue
                    # Check if there's a blocked cell between m and i
                    blocked = False
                    for k in range(m-1, i):
                        if S[k] == 'X':
                            blocked = True
                            break
                    if blocked:
                        continue
                    # Calculate the attraction power
                    dist = m - i
                    sheets = sheet_count[i+1] + sheet_count[m]
                    power = K + 1 - dist - sheets
                    if power > 0:
                        used_m[j] = True
                        count += 1
                        break
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()