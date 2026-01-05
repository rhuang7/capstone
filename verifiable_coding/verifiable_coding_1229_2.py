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
        # We can only swap elements at even indices (Motu's turn) with elements at odd indices (Tomu's turn)
        # Because swapping elements at even indices with elements at odd indices will change the scores
        # We need to find the best K swaps that maximize (Tomu's score - Motu's score)
        # We can do this by considering the difference between elements at even and odd indices
        
        # Create a list of differences (Tomu's gain - Motu's loss) for each possible swap
        diff = []
        for i in range(0, N, 2):
            for j in range(i+1, N, 2):
                # Swap A[i] (Motu's element) with A[j] (Tomu's element)
                # Motu loses A[i], gains A[j]
                # Tomu loses A[j], gains A[i]
                # Difference in scores: (A[i] - A[j]) - (A[j] - A[i]) = 2*(A[i] - A[j])
                diff.append(2 * (A[i] - A[j]))
        
        # Sort the differences in descending order
        diff.sort(reverse=True)
        
        # Apply up to K best swaps
        for i in range(min(K, len(diff))):
            motu_score += diff[i]
            tomu_score += diff[i]
        
        # Check if Tomu wins
        if tomu_score > motu_score:
            results.append("YES")
        else:
            results.append("NO")
    
    for res in results:
        print(res)