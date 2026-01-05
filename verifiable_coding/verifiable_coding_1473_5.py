import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        R = int(data[index])
        C = int(data[index+1])
        M = int(data[index+2])
        K = int(data[index+3])
        J = int(data[index+4])
        index += 5
        
        total = R * C
        if M + K + J != total:
            results.append("No")
            continue
        
        # Function to find all possible rectangles with area a
        def get_rects(area, max_dim):
            rects = []
            for h in range(1, int(area**0.5) + 1):
                if area % h == 0:
                    w = area // h
                    if w <= max_dim:
                        rects.append((h, w))
                    if h <= max_dim:
                        rects.append((w, h))
            return rects
        
        # Get all possible rectangles for each area
        rects_m = get_rects(M, R)
        rects_k = get_rects(K, R)
        rects_j = get_rects(J, R)
        
        # Check all combinations
        found = False
        for m_h, m_w in rects_m:
            rem_r = R - m_h
            rem_c = C - m_w
            if rem_r < 0 or rem_c < 0:
                continue
            for k_h, k_w in rects_k:
                if k_h > rem_r or k_w > rem_c:
                    continue
                rem_r2 = rem_r - k_h
                rem_c2 = rem_c - k_w
                if rem_r2 < 0 or rem_c2 < 0:
                    continue
                for j_h, j_w in rects_j:
                    if j_h > rem_r2 or j_w > rem_c2:
                        continue
                    if j_h * j_w == J:
                        found = True
                        break
                if found:
                    break
            if found:
                break
        results.append("Yes" if found else "No")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()