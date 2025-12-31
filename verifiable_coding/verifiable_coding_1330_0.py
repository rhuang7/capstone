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
        
        # Create a list of tuples (c_i, d_i, i) for all districts
        districts = [(c[i], d[i], i) for i in range(A*B)]
        
        # Sort districts based on the maximum of c_i and d_i in descending order
        districts.sort(key=lambda x: max(x[0], x[1]), reverse=True)
        
        # For each state, select B districts
        count_p1 = 0
        for i in range(0, A*B, B):
            state = districts[i:i+B]
            max_val = -1
            max_party = None
            for dist in state:
                if max(dist[0], dist[1]) > max_val:
                    max_val = max(dist[0], dist[1])
                    max_party = 'P1' if dist[0] == max_val else 'P2'
            if max_party == 'P1':
                count_p1 += 1
        
        results.append(str(count_p1))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()