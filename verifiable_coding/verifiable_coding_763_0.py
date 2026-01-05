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
        
        s_zeros = [i for i in range(N) if S[i] == '0']
        s_ones = [i for i in range(N) if S[i] == '1']
        p_zeros = [i for i in range(N) if P[i] == '0']
        p_ones = [i for i in range(N) if P[i] == '1']
        
        if len(s_zeros) != len(p_zeros) or len(s_ones) != len(p_ones):
            results.append("No")
            continue
        
        # Check if the positions of 0s in S can be moved to the positions of 0s in P
        # by swapping with 1s
        # For each 0 in S, it must be possible to move it to a 0 in P
        # by swapping with 1s
        # So the relative order of 0s in S and P must be the same
        # But since we can swap any 0 with any 1, the relative positions of 0s in S and P must be the same
        # So we can check if the sorted list of 0 positions in S is the same as in P
        # But since we can move 0s around by swapping with 1s, the relative order of 0s in S and P must be the same
        # So we can check if the sorted list of 0 positions in S is the same as in P
        
        s_zeros_sorted = sorted(s_zeros)
        p_zeros_sorted = sorted(p_zeros)
        
        if s_zeros_sorted != p_zeros_sorted:
            results.append("No")
            continue
        
        results.append("Yes")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()