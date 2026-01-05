import sys
import bisect

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
        sequences = []
        for _ in range(N):
            seq = list(map(int, data[idx:idx+N]))
            idx += N
            sequences.append(seq)
        
        # Preprocess each sequence to sort and keep track of original indices
        sorted_seqs = []
        for seq in sequences:
            sorted_seq = sorted(seq)
            sorted_seqs.append(sorted_seq)
        
        # DP table: dp[i][k] = maximum sum for first i sequences with the i-th element being the k-th smallest in the i-th sequence
        dp = [[-1] * N for _ in range(N)]
        for k in range(N):
            dp[0][k] = sorted_seqs[0][k]
        
        for i in range(1, N):
            for k in range(N):
                # Find the smallest value in the i-th sequence that is larger than the value in the (i-1)-th sequence
                # We need to find the smallest value in the i-th sequence that is larger than the value in the (i-1)-th sequence
                # We can use binary search for this
                for prev_k in range(N):
                    if dp[i-1][prev_k] == -1:
                        continue
                    # Find the smallest value in the i-th sequence that is larger than dp[i-1][prev_k]
                    val = dp[i-1][prev_k]
                    pos = bisect.bisect_right(sorted_seqs[i], val)
                    if pos < N:
                        if dp[i][k] == -1 or dp[i-1][prev_k] + sorted_seqs[i][pos] > dp[i][k]:
                            dp[i][k] = dp[i-1][prev_k] + sorted_seqs[i][pos]
        
        max_sum = -1
        for k in range(N):
            if dp[N-1][k] != -1:
                max_sum = max(max_sum, dp[N-1][k])
        results.append(str(max_sum) if max_sum != -1 else "-1")
    
    print("\n".join(results))