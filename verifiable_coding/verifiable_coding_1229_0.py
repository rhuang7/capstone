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
        
        # Calculate initial scores
        motu_score = 0
        tomu_score = 0
        for i in range(N):
            if i % 2 == 0:
                motu_score += A[i]
            else:
                tomu_score += A[i]
        
        # If Tomu already wins, output YES
        if tomu_score > motu_score:
            results.append("YES")
            continue
        
        # If Tomu can't win even with K swaps, output NO
        if K == 0:
            results.append("NO")
            continue
        
        # We can only swap elements at even indices (Motu's turns) with elements at odd indices (Tomu's turns)
        # To maximize Tomu's score, we want to swap elements at even indices with elements at odd indices
        # that are larger than the current element at even index
        # We collect all possible swaps and sort them by the gain in Tomu's score
        swaps = []
        for i in range(0, N, 2):
            for j in range(i+1, N, 2):
                if A[j] > A[i]:
                    gain = A[j] - A[i] + (A[i] - A[j])  # gain for Tomu is (A[j] - A[i]) + (A[i] - A[j]) = 0? Wait, let's think
                    # Wait, when we swap A[i] (Motu's turn) with A[j] (Tomu's turn), the scores change as:
                    # Motu loses A[i] and gains A[j], Tomu loses A[j] and gains A[i]
                    # So Motu's score changes by (A[j] - A[i]), Tomu's score changes by (A[i] - A[j])
                    # So the net change for Tomu is (A[i] - A[j]) - (A[j] - A[i]) = 2*(A[i] - A[j])? No, let's think again
                    # Motu's score: -A[i] + A[j]
                    # Tomu's score: -A[j] + A[i]
                    # So Tomu's score change is (A[i] - A[j])
                    # So the gain for Tomu is (A[i] - A[j])
                    # So we want to maximize this gain
                    gain = A[i] - A[j]
                    if gain > 0:
                        swaps.append((gain, i, j))
        
        # Sort swaps by gain in descending order
        swaps.sort(reverse=True)
        
        # Apply up to K swaps
        for gain, i, j in swaps:
            if K <= 0:
                break
            # Swap A[i] and A[j]
            A[i], A[j] = A[j], A[i]
            K -= 1
        
        # Recalculate scores
        motu_score = 0
        tomu_score = 0
        for i in range(N):
            if i % 2 == 0:
                motu_score += A[i]
            else:
                tomu_score += A[i]
        
        if tomu_score > motu_score:
            results.append("YES")
        else:
            results.append("NO")
    
    for res in results:
        print(res)