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
        
        # Check if it's possible to rearrange into a valid arrangement
        b_count = s.count('B')
        g_count = n - b_count
        if abs(b_count - g_count) > 1:
            results.append("-1")
            continue
        
        # Prepare list of positions for B and G
        B = []
        G = []
        for i, c in enumerate(s):
            if c == 'B':
                B.append(i)
            else:
                G.append(i)
        
        # We need to interleave B and G, so the number of B and G must be equal or differ by 1
        # We will try to arrange them in a way that alternates B and G
        
        # For type 0, cost is 1 per swap
        # For type 1, cost is |i - j|
        # For type 2, cost is (i - j)^2
        
        # We will try to arrange the characters in a valid pattern
        # Let's try to create a valid pattern starting with B or G
        # If it's not possible, we'll try the other
        
        # Try to create a valid pattern starting with B
        valid = False
        pattern = []
        for i in range(n):
            if i % 2 == 0:
                pattern.append('B')
            else:
                pattern.append('G')
        if pattern == list(s):
            results.append("0")
            continue
        # Try to create a valid pattern starting with G
        pattern = []
        for i in range(n):
            if i % 2 == 0:
                pattern.append('G')
            else:
                pattern.append('B')
        if pattern == list(s):
            results.append("0")
            continue
        
        # If neither pattern is valid, we need to find a valid arrangement
        # We will try to create a valid pattern by alternating B and G
        
        # We need to have the same number of B and G or differ by 1
        # Let's try to arrange the B and G in a valid pattern
        
        # Let's create a valid pattern
        valid_pattern = []
        for i in range(n):
            if i % 2 == 0:
                valid_pattern.append('B' if i < len(B) else 'G')
            else:
                valid_pattern.append('G' if i < len(G) else 'B')
        
        # Now, we need to find the minimum cost to convert s to valid_pattern
        # We will use a greedy approach to swap the characters
        
        # For each position, if the character is not correct, we will swap it with the correct one
        # We will track the positions of B and G in the valid pattern
        
        # Prepare the correct positions for B and G in the valid pattern
        correct_B = []
        correct_G = []
        for i in range(n):
            if valid_pattern[i] == 'B':
                correct_B.append(i)
            else:
                correct_G.append(i)
        
        # Now, we need to find the minimum cost to swap the characters to match the valid pattern
        
        # For each B in the original string, if it is not in the correct position, we need to swap it with a G
        # Similarly for G
        
        # We will use two pointers to track the correct positions of B and G
        b_ptr = 0
        g_ptr = 0
        
        cost = 0
        for i in range(n):
            if s[i] == 'B':
                if i == correct_B[b_ptr]:
                    b_ptr += 1
                else:
                    # Swap with the correct G
                    while g_ptr < len(correct_G) and correct_G[g_ptr] != i:
                        g_ptr += 1
                    if g_ptr < len(correct_G):
                        cost += abs(correct_G[g_ptr] - i)
                        # Swap the B and G
                        # We need to find the correct G for this B
                        # We will move the G pointer to the correct position
                        # This is a greedy approach
                        # We will swap the B at i with the G at correct_G[g_ptr]
                        # Then move both pointers
                        g_ptr += 1
                        b_ptr += 1
                    else:
                        # No G found, invalid pattern
                        results.append("-1")
                        break
            else:
                if i == correct_G[g_ptr]:
                    g_ptr += 1
                else:
                    # Swap with the correct B
                    while b_ptr < len(correct_B) and correct_B[b_ptr] != i:
                        b_ptr += 1
                    if b_ptr < len(correct_B):
                        cost += abs(correct_B[b_ptr] - i)
                        # Swap the G at i with the B at correct_B[b_ptr]
                        # Then move both pointers
                        b_ptr += 1
                        g_ptr += 1
                    else:
                        # No B found, invalid pattern
                        results.append("-1")
                        break
        else:
            results.append(str(cost))
            continue
        
        results.append("-1")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()