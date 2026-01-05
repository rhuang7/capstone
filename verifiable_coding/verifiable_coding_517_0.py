import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    
    # Total number of strings of length N is 2^N
    total = pow(2, N, M)
    
    # We need to subtract the number of periodic strings
    # A string is periodic if it can be written as v^n where n >= 2
    # So for each divisor d of N where d < N, we subtract the number of strings of length d that can be repeated to form a string of length N
    
    # We use inclusion-exclusion to avoid overcounting
    # The number of strings of length N that are periodic is sum_{d | N, d < N} (2^d - 1)
    # Because for each divisor d, there are 2^d - 1 strings of length d that are not periodic, and they can be repeated to form a string of length N
    
    # Find all divisors of N except N itself
    divisors = set()
    for i in range(2, N):
        if N % i == 0:
            divisors.add(i)
    
    # Compute the sum of (2^d - 1) for each divisor d
    sum_periodic = 0
    for d in divisors:
        sum_periodic += (pow(2, d, M) - 1) % M
    
    # The answer is total - sum_periodic
    answer = (total - sum_periodic) % M
    print(answer)

if __name__ == '__main__':
    solve()