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
        S = data[idx]
        idx += 1
        
        operations = 0
        for i in range(N - 1):
            if S[i] == S[i + 1]:
                operations += 1
                # Toggle the current bit
                S = S[:i] + ('1' if S[i] == '0' else '0') + S[i+1:]
        
        results.append(str(operations))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()