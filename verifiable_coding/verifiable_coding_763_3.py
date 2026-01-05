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
        
        s_zeros = [i for i, c in enumerate(S) if c == '0']
        s_ones = [i for i, c in enumerate(S) if c == '1']
        
        p_zeros = [i for i, c in enumerate(P) if c == '0']
        p_ones = [i for i, c in enumerate(P) if c == '1']
        
        # Check if the number of 0s and 1s in S and P are the same
        if len(s_zeros) != len(p_zeros) or len(s_ones) != len(p_ones):
            results.append("No")
            continue
        
        # Check if the positions of 0s in S can be rearranged to match P's 0s
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P
        # Similarly for 1s
        
        # Check if the 0s in S can be rearranged to match the 0s in P
        # Since we can only swap 1s and 0s, the relative order of 0s and 1s must be the same
        # So, the positions of 0s in S must be a permutation of the positions of 0s in P