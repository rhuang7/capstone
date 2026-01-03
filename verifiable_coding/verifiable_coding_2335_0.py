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
            pos[p[i]] = i + 1  # positions are 1-based
        
        # Now simulate the process
        # For each step i from 1 to n, check if the position chosen for i is valid
        valid = True
        for i in range(1, n + 1):
            # Find r_j for all j from 1 to n
            # r_j is the minimum index >= j that is not yet occupied
            # We can precompute r_j for all j
            r = [0] * (n + 1)
            for j in range(1, n + 1):
                # Find the first position >= j that is not occupied
                for k in range(j, n + 1):
                    if not occupied[k]:
                        r[j] = k
                        break
                else:
                    r[j] = -1  # not defined
            
            # Now compute count_t for all t
            count = [0] * (n + 1)
            for j in range(1, n + 1):
                if r[j] != -1:
                    count[r[j]] += 1
            
            # Find the positions that are not occupied and have maximum count
            max_count = -1
            candidates = []
            for t in range(1, n + 1):
                if not occupied[t] and count[t] > max_count:
                    max_count = count[t]
                    candidates = [t]
                elif not occupied[t] and count[t] == max_count:
                    candidates.append(t)
            
            # The position chosen for i must be in candidates
            # The position of i in the permutation is pos[i]
            if pos[i] not in candidates:
                valid = False
                break
            
            # Mark the position as occupied
            occupied[pos[i]] = True
        
        results.append("Yes" if valid else "No")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()