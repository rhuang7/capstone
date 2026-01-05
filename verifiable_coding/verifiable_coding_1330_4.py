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
        
        # Combine c and d into pairs and sort them by the maximum of each pair
        districts = []
        for i in range(A*B):
            max_val = max(c[i], d[i])
            districts.append((max_val, c[i], d[i]))
        
        # Sort districts in descending order of max_val
        districts.sort(reverse=True)
        
        # For each state, select B districts such that the maximum in the state is from P1
        # We can greedily select the top districts where the max is from P1
        count = 0
        i = 0
        while i < len(districts):
            # Check if the current district's max is from P1
            if districts[i][1] == districts[i][0]:
                count += 1
                i += B
            else:
                i += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()