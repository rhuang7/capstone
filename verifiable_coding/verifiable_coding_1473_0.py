import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        R = int(data[idx])
        C = int(data[idx+1])
        M = int(data[idx+2])
        K = int(data[idx+3])
        J = int(data[idx+4])
        idx += 5
        
        total = R * C
        if M + K + J != total:
            results.append("No")
            continue
        
        # Function to find all possible dimensions for a given area
        def get_rects(area):
            rects = []
            for h in range(1, int(area**0.5) + 1):
                if area % h == 0:
                    w = area // h
                    rects.append((h, w))
            return rects
        
        # Get all possible rectangles for each area
        rects_m = get_rects(M)
        rects_k = get_rects(K)
        rects_j = get_rects(J)
        
        # Try all combinations of rectangles for M, K, J
        found = False
        for (h1, w1) in rects_m:
            for (h2, w2) in rects_k:
                for (h3, w3) in rects_j:
                    # Check if the rectangles can fit in R x C
                    # Check horizontal and vertical arrangements
                    # Case 1: M and K are stacked vertically
                    if h1 + h2 <= R and w1 <= C and w2 <= C and w1 == w2:
                        if h3 <= R and w3 <= C and w3 == w1 and h3 + h1 + h2 == R:
                            found = True
                            break
                    # Case 2: M and K are stacked horizontally
                    if w1 + w2 <= C and h1 <= R and h2 <= R and h1 == h2:
                        if h3 <= R and w3 <= C and w3 == w1 and h3 + h1 + h2 == R:
                            found = True
                            break
                    # Case 3: M and J are stacked vertically
                    if h1 + h3 <= R and w1 <= C and w3 <= C and w1 == w3:
                        if h2 <= R and w2 <= C and w2 == w1 and h2 + h1 + h3 == R:
                            found = True
                            break
                    # Case 4: M and J are stacked horizontally
                    if w1 + w3 <= C and h1 <= R and h3 <= R and h1 == h3:
                        if h2 <= R and w2 <= C and w2 == w1 and h2 + h1 + h3 == R:
                            found = True
                            break
                    # Case 5: K and J are stacked vertically
                    if h2 + h3 <= R and w2 <= C and w3 <= C and w2 == w3:
                        if h1 <= R and w1 <= C and w1 == w2 and h1 + h2 + h3 == R:
                            found = True
                            break
                    # Case 6: K and J are stacked horizontally
                    if w2 + w3 <= C and h2 <= R and h3 <= R and h2 == h3:
                        if h1 <= R and w1 <= C and w1 == w2 and h1 + h2 + h3 == R:
                            found = True
                            break
                    # Case 7: All three are stacked vertically
                    if h1 + h2 + h3 <= R and w1 <= C and w2 <= C and w3 <= C and w1 == w2 == w3:
                        found = True
                        break
                    # Case 8: All three are stacked horizontally
                    if w1 + w2 + w3 <= C and h1 <= R and h2 <= R and h3 <= R and h1 == h2 == h3:
                        found = True
                        break
                if found:
                    break
            if found:
                break
        results.append("Yes" if found else "No")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()