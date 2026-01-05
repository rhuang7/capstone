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
        type_ = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        
        n = len(s)
        B = s.count('B')
        G = n - B
        
        # Check if it's possible to rearrange
        if abs(B - G) > 1:
            results.append("-1")
            continue
        
        # Prepare lists of positions for B and G
        B_pos = [i for i, c in enumerate(s) if c == 'B']
        G_pos = [i for i, c in enumerate(s) if c == 'G']
        
        # Determine the desired arrangement
        if B == G:
            # Alternating pattern: BGBGBG... or GBGBGB...
            # We need to make sure that the number of B and G are equal
            # So we can choose either pattern
            # We'll try to make it start with B
            desired = ['B' if i % 2 == 0 else 'G' for i in range(n)]
        else:
            # One more B or G
            # We need to make sure that the extra one is placed in a way that doesn't cause two same in a row
            # So we can start with B if B > G, else start with G
            if B > G:
                desired = ['B' if i % 2 == 0 else 'G' for i in range(n)]
            else:
                desired = ['G' if i % 2 == 0 else 'B' for i in range(n)]
        
        # Now, we need to find the minimum cost to convert s to desired
        # We can do this by matching B's to G's positions and vice versa
        # For each B in s, we need to find a G in desired, and vice versa
        # We'll use two pointers to match B's and G's
        
        # Prepare desired positions for B and G
        desired_B = [i for i, c in enumerate(desired) if c == 'B']
        desired_G = [i for i, c in enumerate(desired) if c == 'G']
        
        # Match B's and G's
        i = 0
        j = 0
        cost = 0
        
        while i < len(B_pos) and j < len(G_pos):
            if B_pos[i] < desired_B[i]:
                # This B needs to be swapped with a G that is to the right
                # So we need to swap with the first G that is to the right
                # Find the first G in desired_G that is >= B_pos[i]
                while j < len(G_pos) and G_pos[j] < B_pos[i]:
                    j += 1
                if j < len(G_pos):
                    # Swap B at B_pos[i] with G at G_pos[j]
                    cost += abs(G_pos[j] - B_pos[i]) ** type_
                    i += 1
                    j += 1
                else:
                    # No such G, impossible
                    results.append("-1")
                    break
            else:
                # This B is already in the correct position
                i += 1
        
        else:
            # If we have matched all B's, check if all G's are matched
            if i < len(B_pos) or j < len(G_pos):
                results.append("-1")
            else:
                # All matched, calculate cost
                results.append(str(cost))
        
        # If we broke out of the loop early, we already added -1
        # So continue to next test case
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()