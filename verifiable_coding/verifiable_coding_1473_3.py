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
        
        total_area = R * C
        if M + K + J != total_area:
            results.append("No")
            continue
        
        def get_possible_areas(r, c):
            areas = set()
            for i in range(1, r + 1):
                for j in range(1, c + 1):
                    areas.add(i * j)
            return areas
        
        possible_M = set()
        for i in range(1, R + 1):
            if M % i == 0:
                j = M // i
                if 1 <= j <= C:
                    possible_M.add((i, j))
        
        possible_K = set()
        for i in range(1, R + 1):
            if K % i == 0:
                j = K // i
                if 1 <= j <= C:
                    possible_K.add((i, j))
        
        possible_J = set()
        for i in range(1, R + 1):
            if J % i == 0:
                j = J // i
                if 1 <= j <= C:
                    possible_J.add((i, j))
        
        found = False
        for m_r, m_c in possible_M:
            remaining = R * C - M
            for k_r, k_c in possible_K:
                if k_r > R or k_c > C:
                    continue
                if k_r * k_c != K:
                    continue
                remaining_k = remaining - K
                for j_r, j_c in possible_J:
                    if j_r > R or j_c > C:
                        continue
                    if j_r * j_c != J:
                        continue
                    if (m_r + k_r + j_r) == R and (m_c + k_c + j_c) == C:
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