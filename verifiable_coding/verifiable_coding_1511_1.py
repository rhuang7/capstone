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
        
        # Preprocess: for each position, store the number of sheets to the left and right
        sheet_left = [0] * N
        sheet_right = [0] * N
        sheet_count = 0
        for i in range(N):
            if S[i] == ':':
                sheet_count += 1
            sheet_left[i] = sheet_count
        
        sheet_count = 0
        for i in range(N-1, -1, -1):
            if S[i] == ':':
                sheet_count += 1
            sheet_right[i] = sheet_count
        
        # For each magnet, find all possible irons it can attract
        # And count the maximum matching
        # We'll use a greedy approach: for each iron, try to assign the closest possible magnet
        # That is, for each iron, check if there is a magnet to its left or right that can attract it
        # And if so, assign it to the closest one
        
        # We'll use a list to track which irons are already assigned
        assigned = [False] * N
        
        count = 0
        
        for i in range(N):
            if S[i] == 'I':
                # Check to the left for a magnet that can attract this iron
                left = i - 1
                while left >= 0 and S[left] != 'M':
                    left -= 1
                if left >= 0:
                    # Check if this magnet can attract this iron
                    dist = i - left
                    sheets = sheet_left[i] - sheet_left[left]  # sheets between left and i
                    P = K + 1 - dist - sheets
                    if P > 0:
                        # Check if there are any blocked cells between left and i
                        blocked = False
                        for j in range(left + 1, i):
                            if S[j] == 'X':
                                blocked = True
                                break
                        if not blocked:
                            # Assign this iron to this magnet
                            assigned[i] = True
                            count += 1
                            continue
                
                # Check to the right for a magnet that can attract this iron
                right = i + 1
                while right < N and S[right] != 'M':
                    right += 1
                if right < N:
                    # Check if this magnet can attract this iron
                    dist = right - i
                    sheets = sheet_right[i] - sheet_right[right]  # sheets between i and right
                    P = K + 1 - dist - sheets
                    if P > 0:
                        # Check if there are any blocked cells between i and right
                        blocked = False
                        for j in range(i + 1, right):
                            if S[j] == 'X':
                                blocked = True
                                break
                        if not blocked:
                            # Assign this iron to this magnet
                            assigned[i] = True
                            count += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()