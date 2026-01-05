import sys
import itertools

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        zeros = a.count(0)
        non_zeros = N - zeros
        # The missing numbers are the ones not in a (excluding zeros)
        missing = []
        for i in range(1, N+1):
            if i not in a:
                missing.append(i)
        
        # Generate all possible ways to fill the zeros with the missing numbers
        # Each way is a permutation of the missing numbers of length zeros
        # We'll try all possible permutations of the missing numbers
        # For each permutation, replace the zeros in a with the permutation
        # Then check if the resulting permutation is good
        
        count = 0
        for perm in itertools.permutations(missing):
            # Replace zeros in a with the permutation
            new_a = a.copy()
            zero_idx = 0
            for i in range(N):
                if new_a[i] == 0:
                    new_a[i] = perm[zero_idx]
                    zero_idx += 1
            # Now check if the new_a is a permutation of 1..N
            # (It should be, since we filled in the missing numbers)
            # Now check the number of increasing positions
            inc_count = 0
            for i in range(1, N):
                if new_a[i] > new_a[i-1]:
                    inc_count += 1
            if inc_count == K:
                count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()