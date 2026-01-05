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
        
        total_area = R * C
        if M + K + J != total_area:
            results.append("No")
            continue
        
        def get_possible_areas(area, r, c):
            possible = set()
            for i in range(1, r + 1):
                if area % i == 0:
                    j = area // i
                    if 1 <= j <= c:
                        possible.add((i, j))
            return possible
        
        m_areas = get_possible_areas(M, R, C)
        k_areas = get_possible_areas(K, R, C)
        j_areas = get_possible_areas(J, R, C)
        
        found = False
        for m_r, m_c in m_areas:
            remaining_r = R - m_r
            remaining_c = C
            for k_r, k_c in k_areas:
                if k_r > remaining_r or k_c > remaining_c:
                    continue
                remaining_r2 = remaining_r - k_r
                remaining_c2 = remaining_c - k_c
                for j_r, j_c in j_areas:
                    if j_r > remaining_r2 or j_c > remaining_c2:
                        continue
                    if j_r * j_c == J:
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