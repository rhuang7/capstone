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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        value_indices = {}
        found = False
        
        for i in range(N):
            a = A[i]
            if a not in value_indices:
                value_indices[a] = []
            value_indices[a].append(i)
        
        for key in value_indices:
            indices = value_indices[key]
            if len(indices) >= 2:
                i1 = indices[0]
                i2 = indices[1]
                if A[i1] != A[i2]:
                    found = True
                    break
        
        if found:
            results.append("Truly Happy")
        else:
            results.append("Poor Chef")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()