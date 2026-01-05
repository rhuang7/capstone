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
        
        # Initial scores
        motu_score = 0
        tomu_score = 0
        
        # Calculate initial scores
        for i in range(N):
            if i % 2 == 0:
                motu_score += A[i]
            else:
                tomu_score += A[i]
        
        # If Tomu already wins, output YES
        if tomu_score > motu_score:
            results.append("YES")
            continue
        
        # If Tomu cannot win even with K swaps, output NO
        if K == 0:
            results.append("NO")
            continue
        
        # Create a list of pairs (value, index) for all elements
        elements = [(A[i], i) for i in range(N)]
        
        # Sort elements based on value (descending) for Tomu to maximize his gain
        elements.sort(reverse=True, key=lambda x: x[0])
        
        # Try to perform swaps to maximize Tomu's score
        # We can swap elements at even indices (Motu's turn) with elements at odd indices (Tomu's turn)
        # To maximize Tomu's score, we want to swap elements at even indices with elements at odd indices that are larger
        # We will try to find the best K swaps to maximize the difference between Tomu's and Motu's scores
        
        # Calculate the initial difference
        diff = tomu_score - motu_score
        
        # We will try to find the best K swaps
        # We can only swap elements at even indices with elements at odd indices
        # So we need to consider pairs of elements (even index, odd index)
        # For each such pair, if we swap them, the difference will change by (A[odd] - A[even]) - (A[even] - A[odd]) = 2*(A[odd] - A[even])
        # So we want to find the K pairs with the largest (A[odd] - A[even]) values
        
        # Create a list of possible swaps
        swaps = []
        for i in range(0, N, 2):
            for j in range(i+1, N, 2):
                if i < j:
                    swaps.append((A[j] - A[i], i, j))
        
        # Sort the swaps in descending order of (A[odd] - A[even])
        swaps.sort(reverse=True)
        
        # Try to perform up to K swaps
        for i in range(min(K, len(swaps))):
            val, even_idx, odd_idx = swaps[i]
            # Swap the elements
            A[even_idx], A[odd_idx] = A[odd_idx], A[even_idx]
            # Recalculate the scores
            motu_score = 0
            tomu_score = 0
            for i in range(N):
                if i % 2 == 0:
                    motu_score += A[i]
                else:
                    tomu_score += A[i]
            # Update the difference
            diff = tomu_score - motu_score
        
        # Check if Tomu can win
        if diff > 0:
            results.append("YES")
        else:
            results.append("NO")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()