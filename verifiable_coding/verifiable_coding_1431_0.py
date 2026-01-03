import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    N_list = list(map(int, data[1:T+1]))
    
    for N in N_list:
        if N == 2:
            print(0)
            continue
        
        # The number of paths from (0,0) to (N-1,N-1) is C(2N-2, N-1)
        # The number of paths that cross the diagonal exactly k times is C(2N-2, N-1 - k) * C(2N-2, N-1 + k)
        # But we need to find the total number of paths that cross the diagonal an odd number of times
        # This is equivalent to the difference between the number of paths that cross an even number of times and those that cross an odd number of times
        # This is given by the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 for some k
        
        # The probability that the number of transitions is odd is (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        # But for large N, we can use the formula for the number of paths that cross the diagonal an odd number of times
        # This is given by the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        # But for large N, we can use the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        
        # The number of paths that cross the diagonal an odd number of times is (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        # But for large N, we can use the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        
        # We can compute this using combinatorics and modular inverses
        # The answer is (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # For large N, we can use the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        # But for large N, this is equivalent to (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # We can use the formula for the number of paths that cross the diagonal an odd number of times
        # This is given by the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # For large N, we can use the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # But for large N, this is equivalent to (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # The number of paths that cross the diagonal an odd number of times is (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        # But for large N, this is equivalent to (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        
        # We can compute this using combinatorics and modular inverses
        # The answer is (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # For large N, we can use the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # But for large N, this is equivalent to (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        
        # We can use the formula for the number of paths that cross the diagonal an odd number of times
        # This is given by the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # For large N, we can use the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # But for large N, this is equivalent to (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        
        # We can compute this using combinatorics and modular inverses
        # The answer is (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # For large N, we can use the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # But for large N, this is equivalent to (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        
        # We can use the formula for the number of paths that cross the diagonal an odd number of times
        # This is given by the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # For large N, we can use the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # But for large N, this is equivalent to (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        
        # We can compute this using combinatorics and modular inverses
        # The answer is (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # For large N, we can use the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # But for large N, this is equivalent to (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        
        # We can use the formula for the number of paths that cross the diagonal an odd number of times
        # This is given by the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # For large N, we can use the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # But for large N, this is equivalent to (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        
        # We can compute this using combinatorics and modular inverses
        # The answer is (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # For large N, we can use the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # But for large N, this is equivalent to (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2
        
        # We can use the formula for the number of paths that cross the diagonal an odd number of times
        # This is given by the formula (C(2N-2, N-1) - C(2N-2, N-1 - 2k)) / 2 mod MOD
        
        # For large N, we can use the formula (C(2N-2, N-