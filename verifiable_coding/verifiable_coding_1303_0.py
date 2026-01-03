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
        
        # For each position i (1-based), compute A[i-1] % M
        # And group elements by their (i % M) value
        # We need to select K elements such that the i-th element in the subsequence satisfies A[i-1] % M == i % M
        # So for position j in the subsequence (1-based), the element must satisfy A[i-1] % M == j % M
        # So we can precompute for each position in the array, what (i % M) value it contributes to
        # Then, for each possible j (1-based in the subsequence), we can count how many elements in the array have (i % M) == j % M
        # Then, the problem reduces to choosing K elements such that for each position j in the subsequence, the j-th element in the subsequence comes from the group of elements with (i % M) == j % M
        # This is a combinatorial problem: for each j in 1..K, we choose one element from the group of elements with (i % M) == j % M
        # So we can precompute for each j in 1..K, the count of elements in the array with (i % M) == j % M
        # Then, the answer is the product of these counts for each j in 1..K
        # But we need to make sure that for each j, there are enough elements in the group to choose from
        # So we can precompute for each j in 1..K, the count of elements in the array with (i % M) == j % M
        # Then, the answer is the product of these counts for each j in 1..K
        
        # Precompute for each j in 1..K, the count of elements in the array with (i % M) == j % M
        count = [0] * M
        for i in range(N):
            rem = A[i] % M
            count[rem] += 1
        
        # Now, for each j in 1..K, we need to select one element from the group with (i % M) == j % M
        # So the answer is the product of count[j % M] for j in 1..K
        # But we need to make sure that for each j, count[j % M] >= 1
        # If any of them is zero, the answer is zero
        ans = 1
        for j in range(1, K+1):
            rem = j % M
            if count[rem] == 0:
                ans = 0
                break
            ans = (ans * count[rem]) % MOD
        results.append(ans)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()