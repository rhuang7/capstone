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
        
        # Replace -1 with possible values
        # We need to find the maximum possible K such that A is a contiguous subsequence of some periodic sequence
        # The periodic sequence is defined as S_i = (i % K) + 1
        
        # First, check if all elements are -1
        if all(x == -1 for x in A):
            results.append("inf")
            continue
        
        # Find all possible positions where -1 occurs
        unknown_positions = [i for i in range(N) if A[i] == -1]
        
        # For each unknown position, try to fill it with a value that is consistent with the periodic sequence
        # The maximum possible K is N, since the sequence is of length N
        # We need to check all possible K from 1 to N and see if it's valid
        
        max_k = -1
        possible = False
        
        for K in range(1, N+1):
            # Check if the sequence A can be filled with values such that it is a contiguous subsequence of a periodic sequence with period K
            # For each position i in A, if it's not -1, it must be equal to (i % K) + 1
            # If it's -1, we can fill it with any value that is consistent with the periodic sequence
            
            # Check if the sequence is valid for this K
            valid = True
            for i in range(N):
                if A[i] != -1:
                    if (i % K) + 1 != A[i]:
                        valid = False
                        break
            if valid:
                possible = True
                max_k = K
        
        if possible:
            results.append(str(max_k))
        else:
            results.append("impossible")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()