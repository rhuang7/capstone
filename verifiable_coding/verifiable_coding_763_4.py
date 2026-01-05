import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        S = data[index]
        index += 1
        P = data[index]
        index += 1
        
        # Check if S and P have the same number of 1s and 0s
        if S.count('1') != P.count('1'):
            results.append("No")
            continue
        
        # Check if S can be transformed into P with allowed operations
        # Allowed operations: swap a '1' with a '0' (i < j)
        # This means that the relative positions of 1s and 0s must be compatible
        # We can check if for each position, the number of 1s in S up to that position
        # is equal to the number of 1s in P up to that position
        
        s_ones = [0] * (N + 1)
        p_ones = [0] * (N + 1)
        
        for i in range(N):
            s_ones[i + 1] = s_ones[i] + (1 if S[i] == '1' else 0)
            p_ones[i + 1] = p_ones[i] + (1 if P[i] == '1' else 0)
        
        possible = True
        for i in range(1, N + 1):
            if s_ones[i] != p_ones[i]:
                possible = False
                break
        
        results.append("Yes" if possible else "No")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()