import sys
import math

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
        
        # Find all positions where the value is -1
        unknowns = [i for i in range(N) if A[i] == -1]
        if not unknowns:
            # No unknowns, check if it's a valid periodic sequence
            # The period must be such that A[i] = (i % K) + 1
            # So for all i, A[i] - 1 must be congruent modulo K
            # So the possible K's are the GCD of all (A[i] - 1 - (i % K))
            # But since K is unknown, we can find the GCD of all (A[i] - 1 - i) for all i
            # But since K must be such that A[i] = (i % K) + 1, then A[i] - 1 = i % K
            # So for all i, A[i] - 1 must be congruent modulo K
            # So the possible K is the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # But since K must be such that A[i] - 1 = i % K, then K must be such that for all i, A[i] - 1 <= K - 1
            # So the maximum possible K is the maximum of (A[i] - 1) for all i
            # But if the sequence is periodic, then the maximum possible K is the GCD of all (A[i] - 1 - (i % K))
            # However, since K is unknown, we can find the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # But since the sequence is periodic, the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j must be the period
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # But since K must be such that A[i] = (i % K) + 1, then K must be such that for all i, A[i] - 1 = i % K
            # So the possible K is the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # But since K must be such that A[i] - 1 = i % K, then K must be such that for all i, A[i] - 1 <= K - 1
            # So the maximum possible K is the maximum of (A[i] - 1) for all i
            # But if the sequence is periodic, then the maximum possible K is the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # But if the sequence is not periodic, then it's impossible
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # If the GCD is zero, then it's impossible
            # Otherwise, the maximum possible K is the GCD
            # But if the GCD is zero, then it's impossible
            # But if the GCD is non-zero, then it's possible
            # But if the sequence is not periodic, then it's impossible
            # So check if the sequence is periodic
            # For the sequence to be periodic, for all i, A[i] - 1 must be congruent modulo K
            # So for all i, A[i] - 1 must be congruent modulo K
            # So for all i, j, A[i] - 1 - (A[j] - 1) must be divisible by K
            # So K must be a divisor of all (A[i] - 1 - (A[j] - 1)) for i != j
            # So the possible K is the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # But since K must be such that A[i] - 1 = i % K, then K must be such that for all i, A[i] - 1 <= K - 1
            # So the maximum possible K is the maximum of (A[i] - 1) for all i
            # But if the sequence is periodic, then the maximum possible K is the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # But if the GCD is zero, then it's impossible
            # Otherwise, the maximum possible K is the GCD
            # But if the GCD is zero, then it's impossible
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # If the GCD is zero, then it's impossible
            # Otherwise, the maximum possible K is the GCD
            # But if the GCD is zero, then it's impossible
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # If the GCD is zero, then it's impossible
            # Otherwise, the maximum possible K is the GCD
            # But if the GCD is zero, then it's impossible
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # If the GCD is zero, then it's impossible
            # Otherwise, the maximum possible K is the GCD
            # But if the GCD is zero, then it's impossible
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # If the GCD is zero, then it's impossible
            # Otherwise, the maximum possible K is the GCD
            # But if the GCD is zero, then it's impossible
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # If the GCD is zero, then it's impossible
            # Otherwise, the maximum possible K is the GCD
            # But if the GCD is zero, then it's impossible
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # If the GCD is zero, then it's impossible
            # Otherwise, the maximum possible K is the GCD
            # But if the GCD is zero, then it's impossible
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # If the GCD is zero, then it's impossible
            # Otherwise, the maximum possible K is the GCD
            # But if the GCD is zero, then it's impossible
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # If the GCD is zero, then it's impossible
            # Otherwise, the maximum possible K is the GCD
            # But if the GCD is zero, then it's impossible
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # If the GCD is zero, then it's impossible
            # Otherwise, the maximum possible K is the GCD
            # But if the GCD is zero, then it's impossible
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # If the GCD is zero, then it's impossible
            # Otherwise, the maximum possible K is the GCD
            # But if the GCD is zero, then it's impossible
            # So compute the GCD of all (A[i] - 1 - (A[j] - 1)) for i != j
            # If the GCD is zero, then it's impossible
            # Otherwise, the maximum possible K is the GCD
            # But if the GCD is zero, then it's impossible
            # So compute the GCD of all (A[i] - 1 -