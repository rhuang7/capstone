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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # We need to compute the maximum and minimum possible values of the expression
        # after optimally choosing + or - for each operator
        # Since the first player (Vanja) wants to maximize |V| and the second player (Miksi) wants to minimize it
        # We can use dynamic programming to track the possible values
        
        # dp[i][0] = maximum value achievable with i operations and the last operation being +
        # dp[i][1] = minimum value achievable with i operations and the last operation being -
        # But since the operations are applied in sequence, we can track the possible values at each step
        
        # Initialize the possible values after 0 operations (just the first element)
        possible = [A[0]]
        
        for i in range(1, N):
            new_possible = []
            for val in possible:
                new_possible.append(val + A[i])
                new_possible.append(val - A[i])
            possible = new_possible
        
        # The maximum and minimum values after all operations
        max_val = max(possible)
        min_val = min(possible)
        
        if abs(max_val) >= K or abs(min_val) >= K:
            results.append(1)
        else:
            results.append(2)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()