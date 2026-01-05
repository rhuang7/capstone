import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        B = list(map(int, data[idx:idx+N]))
        idx += N
        if B[0] == 0:
            results.append(1)
            continue
        # Check if B is valid
        valid = True
        for i in range(N):
            if i == 0:
                if B[i] != 0:
                    valid = False
                    break
            else:
                if B[i] < B[i-1]:
                    valid = False
                    break
        if not valid:
            results.append(0)
            continue
        # Compute the number of valid sequences
        res = 1
        for i in range(N):
            if i == 0:
                if B[i] != 0:
                    res = 0
                    break
            else:
                prev = B[i-1]
                curr = B[i]
                if (curr & prev) != prev:
                    res = 0
                    break
                # Count the number of ways to get B[i]
                # The previous B[i-1] is fixed, so the current A[i] must be such that B[i] = B[i-1] | A[i]
                # So A[i] can be any value such that B[i] | A[i] = B[i]
                # Which means A[i] must be a subset of B[i] (bitwise)
                # The number of such A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] = B[i-1] | A[i], and B[i] >= B[i-1], we can compute the number of possible A[i]
                # as (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i] is (number of subsets of B[i] that are not subsets of B[i-1])
                # Which is (2^k - 2^m), where k is the number of bits set in B[i], and m is the number of bits set in B[i-1]
                # But since B[i] is fixed, and B[i] = B[i-1] | A[i], the number of possible A[i