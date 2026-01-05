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
        
        # For each value from 1 to n, check if it can be placed in the correct position according to the rules
        valid = True
        for i in range(1, n + 1):
            # Find r_j for all j from 1 to i
            # r_j is the minimum index >= j that is not yet occupied
            # We'll compute r for each j from 1 to i
            # But since we're checking the permutation, we can directly check the position of i in the permutation
            # and see if it satisfies the rules
            # We'll simulate the process
            # For the current value i, check if its position in the permutation is valid
            current_pos = pos[i]
            # Check if this position is valid according to the rules
            # For each j from 1 to i, compute r_j and count_t
            # But since we're checking the permutation, we can directly check the position of i
            # and see if it's a valid choice according to the rules
            # We'll simulate the process for each step
            # For the current value i, check if its position in the permutation is valid
            # We'll track which positions are occupied
            occupied = [False] * (n + 1)  # 1-based indexing
            # For each value from 1 to i-1, mark their positions as occupied
            for j in range(1, i):
                occupied[pos[j]] = True
            # Now compute r_j for j from 1 to i
            # r_j is the minimum index >= j that is not yet occupied
            # We'll compute count_t for each t
            count = [0] * (n + 1)
            for j in range(1, i + 1):
                # find r_j for j
                r_j = None
                for k in range(j, n + 1):
                    if not occupied[k]:
                        r_j = k
                        break
                if r_j is not None:
                    count[r_j] += 1
            # Now find the positions that are not occupied and have maximum count
            max_count = -1
            candidates = []
            for t in range(1, n + 1):
                if not occupied[t] and count[t] > max_count:
                    max_count = count[t]
                    candidates = [t]
                elif not occupied[t] and count[t] == max_count:
                    candidates.append(t)
            # Check if the current position of i is in the candidates
            if current_pos not in candidates:
                valid = False
                break
        
        results.append("Yes" if valid else "No")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()