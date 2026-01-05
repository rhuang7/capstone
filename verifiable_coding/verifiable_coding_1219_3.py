import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        
        # Calculate the number of ways to fill the boxes
        # Boxes at even positions are empty, so we only consider boxes at odd positions
        # Each odd box i has i partitions, and each partition can hold one jewel of any type
        # So for each odd box i, there are M^i ways to fill it
        # Total is product of M^i for all odd i from 1 to N
        
        # Compute the product of M^i for i in 1, 3, 5, ..., up to N (if N is odd)
        # This is equivalent to M^(1 + 3 + 5 + ... + k) where k is the largest odd <= N
        # The sum of first k odd numbers is k^2
        # So the exponent is (number of odd numbers up to N)^2
        
        # Number of odd numbers up to N is (N + 1) // 2
        k = (N + 1) // 2
        exponent = k * k
        result = pow(M, exponent, MOD)
        print(result)

if __name__ == '__main__':
    solve()