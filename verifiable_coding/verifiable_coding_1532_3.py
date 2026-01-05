import sys
MOD = 10**9 + 7

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
        max_numbers = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_numbers.sort()
        # Check if it's possible to assign distinct numbers
        for i in range(N):
            if max_numbers[i] < i + 1:
                results.append(0)
                break
        else:
            # Calculate the number of ways
            # We need to count the number of permutations of N distinct numbers
            # where each number is <= max_numbers[i]
            # This is equivalent to the number of permutations of N distinct numbers
            # that can be chosen from the sorted max_numbers
            # We can use dynamic programming to calculate this
            dp = [0] * (N + 1)
            dp[0] = 1
            for i in range(N):
                for j in range(i, N):
                    dp[j + 1] = (dp[j + 1] + dp[j] * (max_numbers[i] - i)) % MOD
            results.append(dp[N])
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()