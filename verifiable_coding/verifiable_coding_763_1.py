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
        P = data[idx]
        idx += 1
        
        if S == P:
            results.append("Yes")
            continue
        
        count_S_0 = S.count('0')
        count_S_1 = S.count('1')
        count_P_0 = P.count('0')
        count_P_1 = P.count('1')
        
        if count_S_0 != count_P_0 or count_S_1 != count_P_1:
            results.append("No")
            continue
        
        # Check if the positions of 1s in S can be rearranged to match P
        # We need to check if for each position, the number of 1s in S up to that position is >= the number of 1s in P up to that position
        # This is similar to the problem of checking if one string can be transformed into another with certain operations
        
        s_ones = []
        p_ones = []
        
        for i in range(N):
            if S[i] == '1':
                s_ones.append(i)
            if P[i] == '1':
                p_ones.append(i)
        
        # Check if the positions of 1s in S can be rearranged to match P
        # This is possible if for every i, the number of 1s in S up to i is >= the number of 1s in P up to i
        # We can do this by comparing the sorted positions of 1s
        
        if s_ones == p_ones:
            results.append("Yes")
        else:
            results.append("No")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()