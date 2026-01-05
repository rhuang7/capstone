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
                for j in range(1, c + 1):
                    areas.add(i * j)
            return areas
        
        possible_m = set()
        for i in range(1, R + 1):
            if M % i == 0:
                j = M // i
                if j <= C:
                    possible_m.add((i, j))
        possible_k = set()
        for i in range(1, R + 1):
            if K % i == 0:
                j = K // i
                if j <= C:
                    possible_k.add((i, j))
        possible_j = set()
        for i in range(1, R + 1):
            if J % i == 0:
                j = J // i
                if j <= C:
                    possible_j.add((i, j))
        
        found = False
        for m in possible_m:
            remaining = R * C - M
            for k in possible_k:
                if k[0] > R or k[1] > C:
                    continue
                remaining_k = remaining - K
                if remaining_k < 0:
                    continue
                for j in possible_j:
                    if j[0] > R or j[1] > C:
                        continue
                    if m[0] + k[0] + j[0] <= R and m[1] + k[1] + j[1] <= C:
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