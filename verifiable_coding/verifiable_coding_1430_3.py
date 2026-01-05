import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        if K == 0:
            results.append(N)
            continue
        
        # The minimum configuration is to have each kid get at least 1 candy,
        # and alternate between 1 and 1 + K to ensure a difference of at least K
        # between adjacent kids.
        # The pattern is 1, 1 + K, 1 + 2K, ..., 1 + (N-1)K
        # But since it's a circle, the first and last must also differ by at least K.
        # So we need to check if the first and last differ by at least K.
        # If not, we need to adjust the last value.
        
        # Start with 1 for the first kid
        candies = [1] * N
        
        # Alternate between 1 and 1 + K
        for i in range(1, N):
            candies[i] = candies[i - 1] + K
        
        # Check if the first and last differ by at least K
        if candies[0] >= candies[-1]:
            candies[-1] += K
        
        total = sum(candies)
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()