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
        
        s_ones = [i for i in range(N) if S[i] == '1']
        p_ones = [i for i in range(N) if P[i] == '1']
        
        if len(s_ones) != len(p_ones):
            results.append("No")
            continue
        
        # Check if the positions of 1s in S can be rearranged to match P
        # We can sort the positions of 1s in both S and P and compare
        s_ones.sort()
        p_ones.sort()
        
        if s_ones != p_ones:
            results.append("No")
        else:
            results.append("Yes")
    
    print('\n'.join(results))