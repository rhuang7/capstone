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
        L = int(data[idx+1])
        R = int(data[idx+2])
        idx += 3
        
        # Minimum sum: use as many 1s as possible, and one more element to reach L unique
        # Since 1 is always present, we need (L-1) more unique numbers, which must be even numbers
        # The minimum sum is when we have L unique numbers, all as small as possible
        # The smallest L unique numbers are 1, 2, 4, 8, ..., 2^(L-2)
        # So the minimum sum is sum(1 + 2 + 4 + ... + 2^(L-2)) + (N - L) * 1
        min_sum = 0
        for i in range(L):
            if i == 0:
                min_sum += 1
            else:
                min_sum += 2 ** (i - 1)
        min_sum += (N - L) * 1
        
        # Maximum sum: use as many large numbers as possible, with each number being double the previous
        # The maximum sum is when we have R unique numbers, all as large as possible
        # The largest R unique numbers are 2^R, 2^(R-1), ..., 2^0
        # So the maximum sum is sum(2^R + 2^(R-1) + ... + 2^0) - (N - R) * 1
        max_sum = 0
        for i in range(R, -1, -1):
            max_sum += 2 ** i
        max_sum -= (N - R) * 1
        
        results.append(f"{min_sum} {max_sum}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()