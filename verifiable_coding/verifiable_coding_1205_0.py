import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    total = 0

    for S in cases:
        n = len(S)
        total += n * (n - 1) // 2  # Total number of pairs (L, R) is n*(n+1)/2, but we need to subtract the cases where L=R

        # For each position i, count the number of times it contributes to the sum
        # A position i contributes to the sum if it is part of a range [L, R] where the flip changes the adjacent pairs
        # We need to find the number of ranges [L, R] that include i and i+1, and where the flip changes the value at i and i+1
        # This is equivalent to counting the number of ranges [L, R] that include i and i+1, and where the original values at i and i+1 are different

        # For each i from 0 to n-2:
        # if S[i] != S[i+1], then the number of ranges [L, R] that include i and i+1 is (i+1) * (n - i)
        # because L can be from 1 to i+1 and R can be from i+1 to n

        for i in range(n - 1):
            if S[i] != S[i+1]:
                total += (i + 1) * (n - i)

    print(total)

if __name__ == '__main__':
    solve()