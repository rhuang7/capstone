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
        
        # Check if S can be transformed into P using allowed operations
        # Allowed operations: swap a '1' with a '0' (i < j)
        # This is possible if for every position, the number of 1s in S up to that position is >= the number of 1s in P up to that position
        # and the number of 0s in S up to that position is <= the number of 0s in P up to that position
        
        # Count the number of 1s and 0s in S and P
        s_ones = 0
        s_zeros = 0
        p_ones = 0
        p_zeros = 0
        
        for i in range(N):
            if S[i] == '1':
                s_ones += 1
            else:
                s_zeros += 1
            if P[i] == '1':
                p_ones += 1
            else:
                p_zeros += 1
        
        # Check if the counts of 1s and 0s match
        if s_ones != p_ones or s_zeros != p_zeros:
            results.append("No")
            continue
        
        # Check if S can be transformed into P
        s_ones_count = 0
        p_ones_count = 0
        valid = True
        
        for i in range(N):
            if S[i] == '1':
                s_ones_count += 1
            if P[i] == '1':
                p_ones_count += 1
            
            if s_ones_count < p_ones_count:
                valid = False
                break
        
        if valid:
            results.append("Yes")
        else:
            results.append("No")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()