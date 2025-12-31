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
        
        # Compute initial scores
        motu_score = 0
        tomu_score = 0
        for i in range(0, N, 2):
            motu_score += A[i]
        for i in range(1, N, 2):
            tomu_score += A[i]
        
        # If Tomu already wins, output YES
        if tomu_score > motu_score:
            results.append("YES")
            continue
        
        # If Tomu cannot win even with K swaps, output NO
        if K == 0:
            results.append("NO")
            continue
        
        # Find the best swaps to maximize Tomu's score and minimize Motu's score
        # We can only swap elements at even indices (Motu's turns) with elements at odd indices (Tomu's turns)
        # Because swapping an even index with an odd index will change the scores
        # We need to find the best K swaps to maximize the difference (Tomu_score - Motu_score)
        
        # Create a list of possible swaps
        swaps = []
        for i in range(0, N, 2):
            for j in range(i + 1, N, 2):
                # Swap A[i] (Motu's element) with A[j] (Tomu's element)
                # The change in scores is: (A[j] - A[i]) for Motu and (A[i] - A[j]) for Tomu
                # So the net change is (A[j] - A[i]) - (A[i] - A[j]) = 2*(A[j] - A[i])
                # We want to maximize this value, so we look for the largest (A[j] - A[i])
                # So we sort the possible swaps by (A[j] - A[i]) in descending order
                swaps.append((A[j] - A[i], i, j))
        
        # Sort the swaps in descending order of (A[j] - A[i])
        swaps.sort(reverse=True)
        
        # Apply up to K best swaps
        for diff, i, j in swaps:
            if K <= 0:
                break
            # Swap A[i] and A[j]
            A[i], A[j] = A[j], A[i]
            # Update scores
            motu_score -= A[i]
            motu_score += A[j]
            tomu_score -= A[j]
            tomu_score += A[i]
            K -= 1
        
        # Check if Tomu wins
        if tomu_score > motu_score:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))