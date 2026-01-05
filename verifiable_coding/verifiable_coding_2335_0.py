import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        # For each position, find the earliest position >= current value that is not yet occupied
        # We'll track which positions are occupied
        occupied = [False] * (n + 1)  # 1-based indexing
        # For each value from 1 to n, find its position in the permutation
        pos = [0] * (n + 1)  # pos[i] is the position of value i in the permutation
        for i in range(n):
            pos[p[i]] = i + 1  # 1-based position
        
        # For each step i (from 1 to n), check if the current permutation is valid
        valid = True
        for i in range(1, n + 1):
            # Find r_j for all j from 1 to i
            # r_j is the minimum index >= j that is not yet occupied
            # We'll track for each j from 1 to i, the r_j
            # But since we're simulating the process, we can find for each value i, the position it was placed
            # We need to check if the position chosen for i is valid according to the rules
            # For this, we need to find for each j from 1 to i, the r_j
            # Then compute count_t for each t, and select the position with maximum count_t
            # But since we already have the permutation, we can simulate this
            
            # Find for each j from 1 to i, the r_j
            # r_j is the minimum index >= j that is not yet occupied
            # We'll use a list to track the r_j for each j
            r = [0] * (n + 1)  # r[j] is the r_j for j
            for j in range(1, i + 1):
                # Find the minimum index >= j that is not yet occupied
                for k in range(j, n + 1):
                    if not occupied[k]:
                        r[j] = k
                        break
                else:
                    # No such position, r_j is undefined
                    r[j] = -1
            
            # Compute count_t for each t
            count = [0] * (n + 1)
            for j in range(1, i + 1):
                if r[j] != -1:
                    count[r[j]] += 1
            
            # Find the positions that are not yet occupied
            # These are the positions that are available for placing i
            available = [t for t in range(1, n + 1) if not occupied[t]]
            
            # For each available position, check if it has the maximum count
            max_count = -1
            selected_pos = -1
            for t in available:
                if count[t] > max_count:
                    max_count = count[t]
                    selected_pos = t
                elif count[t] == max_count:
                    # If there are multiple positions with the same max count, the generator can choose any
                    # So we need to check if the position chosen in the permutation is one of them
                    # But since we are checking if the permutation is valid, we need to see if the position of i is among them
                    # So we need to check if the position of i is one of the positions with max count
                    # But since we are simulating, we can check if the position of i is among the available positions with max count
                    # So we need to check if the position of i is in the available positions with max count
                    # So we need to check if the position of i is in the available positions with max count
                    # So we need to check if the position of i is in the available positions with max count
                    # So we need to check if the position of i is in the available positions with max count
                    # So we need to check if the position of i is in the available positions with max count
                    # So we need to check if the position of i is in the available positions with max count
                    # So we need to check if the position of i is in the available positions with max count
                    # So we need to check if the position of i is in the available positions with max count
                    pass
            
            # The position of i in the permutation is pos[i]
            # Check if it is one of the positions with max count
            # So check if pos[i] is in the available positions with max count
            # To do this, we can check if count[pos[i]] == max_count and pos[i] is in available
            if count[pos[i]] != max_count or pos[i] not in available:
                valid = False
                break
            
            # Mark the position as occupied
            occupied[pos[i]] = True
        
        results.append("Yes" if valid else "No")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()