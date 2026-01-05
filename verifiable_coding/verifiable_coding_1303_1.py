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
        N, K, M = map(int, data[idx:idx+3])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # For each position i (1-based), we determine what value of (A_j % M) is allowed
        # For position i in the subsequence, A_j % M must equal i % M
        # So for each position i in 1..K, we need to collect elements that satisfy A_j % M == i % M
        # We can precompute for each position i in 1..K, the count of elements in A that satisfy A_j % M == i % M
        
        # Precompute for each position i in 1..K, the count of elements in A that satisfy A_j % M == i % M
        counts = [0] * (K + 1)  # 1-based indexing for positions 1..K
        for a in A:
            rem = a % M
            for i in range(1, K + 1):
                if rem == i % M:
                    counts[i] += 1
        
        # Now, we need to compute the number of ways to choose one element from each of the K groups
        # The groups are determined by the position in the subsequence (i from 1 to K)
        # For each i, we have counts[i] elements that can be used in position i
        # The total number of valid subsequences is the product of counts[i] for i in 1..K
        
        # But we need to make sure that for each i, there are at least 1 element in counts[i]
        # Because we need to choose one element from each group
        # If any counts[i] is 0, then there are 0 valid subsequences
        
        # Compute the product
        res = 1
        for i in range(1, K + 1):
            if counts[i] == 0:
                res = 0
                break
            res = (res * counts[i]) % MOD
        
        results.append(res)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()