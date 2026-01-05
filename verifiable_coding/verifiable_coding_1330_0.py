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
        A = int(data[idx])
        B = int(data[idx+1])
        idx += 2
        c = list(map(int, data[idx:idx+A*B]))
        idx += A*B
        d = list(map(int, data[idx:idx+A*B]))
        idx += A*B
        
        # Combine c and d into pairs and sort by the maximum of each pair
        districts = []
        for i in range(A*B):
            districts.append((c[i], d[i]))
        
        # Sort districts based on the maximum of (c[i], d[i])
        districts.sort(key=lambda x: max(x[0], x[1]), reverse=True)
        
        # For each state, select B districts
        count_p1 = 0
        for i in range(0, A*B, B):
            max_val = -1
            max_party = ''
            for j in range(i, i+B):
                if max(districts[j][0], districts[j][1]) > max_val:
                    max_val = max(districts[j][0], districts[j][1])
                    if districts[j][0] == max_val:
                        max_party = 'P1'
                    else:
                        max_party = 'P2'
            if max_party == 'P1':
                count_p1 += 1
        
        results.append(str(count_p1))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()