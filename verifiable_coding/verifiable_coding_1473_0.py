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
        
        def get_possible_areas(r, c):
            areas = set()
            for i in range(1, r + 1):
                areas.add(i * c)
            for i in range(1, c + 1):
                areas.add(r * i)
            return areas
        
        m_areas = get_possible_areas(R, C)
        k_areas = get_possible_areas(R, C)
        j_areas = get_possible_areas(R, C)
        
        found = False
        for m in m_areas:
            if m == M:
                for k in k_areas:
                    if k == K:
                        remaining = total_area - m - k
                        if remaining == J:
                            found = True
                            break
                if found:
                    break
        results.append("Yes" if found else "No")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()