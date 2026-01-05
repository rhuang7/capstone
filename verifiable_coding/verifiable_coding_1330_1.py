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
        
        # Sort districts based on the maximum value in each pair
        districts.sort(key=lambda x: max(x[0], x[1]), reverse=True)
        
        # For each state, select B districts, and check if the maximum is from P1
        count = 0
        i = 0
        while i < A*B:
            state = []
            max_val = -1
            max_party = ''
            for j in range(i, i+B):
                state.append(districts[j])
                current_max = max(state[0][0], state[0][1])
                if current_max > max_val:
                    max_val = current_max
                    max_party = 'P1' if state[0][0] == max_val else 'P2'
            # Check if the max in this state is from P1
            count += 1 if max_party == 'P1' else 0
            i += B
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()